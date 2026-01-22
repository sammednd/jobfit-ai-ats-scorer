import re
from collections import Counter

STOPWORDS = {
    "and", "or", "the", "a", "an", "to", "for", "in", "on", "with", "of", "is", "are",
    "as", "by", "at", "from", "this", "that", "it", "be", "will", "you", "your", "we",
    "our", "they", "their", "have", "has", "had", "not", "but", "if", "then", "than",
}

def tokenize(text: str):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9\-\+\.]{1,}", text.lower())
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    return words

def extract_keywords(text: str, top_k: int = 30):
    tokens = tokenize(text)
    counts = Counter(tokens)
    return [w for w, _ in counts.most_common(top_k)]

def compute_missing_keywords(jd_keywords, resume_keywords, top_k=10):
    resume_set = set(resume_keywords)
    matched = [k for k in jd_keywords if k in resume_set]
    missing = [k for k in jd_keywords if k not in resume_set]
    return matched[:top_k], missing[:top_k]

def suggest_bullets(missing_keywords):
    bullets = []
    base_templates = [
        "Implemented {kw}-driven solutions to improve delivery quality and reduce manual effort.",
        "Built scalable pipelines integrating {kw} to enhance reliability and performance.",
        "Collaborated with cross-functional teams to apply {kw} in production workflows.",
        "Optimized existing systems by introducing {kw} best practices and monitoring.",
        "Delivered measurable improvements by leveraging {kw} across key project modules.",
    ]
    for i, kw in enumerate(missing_keywords[:5]):
        bullets.append(base_templates[i % len(base_templates)].format(kw=kw))
    return bullets
