import logging
from fastapi import UploadFile
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.config import settings
from utils.pdf import extract_text_from_pdf_bytes
from utils.text import clean_text, make_preview
from utils.keywords import extract_keywords, compute_missing_keywords, suggest_bullets

logger = logging.getLogger("services.matcher")

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        logger.info("Loading embedding model: %s", settings.EMBEDDING_MODEL_NAME)
        _model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)
    return _model

def score_embeddings(resume_text: str, jd_text: str) -> float:
    model = get_embedding_model()
    emb = model.encode([resume_text, jd_text], normalize_embeddings=True)
    sim = float((emb[0] @ emb[1]))
    return round(sim * 100, 2)

def score_tfidf(resume_text: str, jd_text: str) -> float:
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X = vectorizer.fit_transform([resume_text, jd_text])
    sim = cosine_similarity(X[0], X[1])[0][0]
    return round(float(sim) * 100, 2)

async def run_match(resume_pdf: UploadFile, job_description: str, use_tfidf: bool = True) -> dict:
    pdf_bytes = await resume_pdf.read()
    resume_raw = extract_text_from_pdf_bytes(pdf_bytes)
    jd_raw = job_description

    resume_text = clean_text(resume_raw)
    jd_text = clean_text(jd_raw)

    if len(resume_text) < 50:
        raise ValueError("Resume text extraction failed or too short.")

    score_emb = score_embeddings(resume_text, jd_text)
    score_t = score_tfidf(resume_text, jd_text) if use_tfidf else None

    jd_keywords = extract_keywords(jd_text, top_k=40)
    resume_keywords = extract_keywords(resume_text, top_k=60)

    matched, missing = compute_missing_keywords(jd_keywords, resume_keywords, top_k=settings.TOP_K_KEYWORDS)

    bullets = suggest_bullets(missing[:10])

    result = {
        "match_score_embeddings": score_emb,
        "match_score_tfidf": score_t,
        "top_matched_keywords": matched[:settings.TOP_K_KEYWORDS],
        "missing_keywords": missing[:settings.TOP_K_KEYWORDS],
        "suggested_bullets": bullets,
        "resume_text_preview": make_preview(resume_text),
        "jd_text_preview": make_preview(jd_text),
    }

    logger.info("Match computed | emb=%s tfidf=%s", score_emb, score_t)
    return result
