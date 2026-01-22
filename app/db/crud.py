import logging
from app.db.database import SessionLocal
from app.db.models import MatchRun

logger = logging.getLogger("db.crud")

def save_run(result: dict):
    db = SessionLocal()
    try:
        run = MatchRun(
            score_embeddings=result["match_score_embeddings"],
            score_tfidf=result.get("match_score_tfidf"),
            matched_keywords=", ".join(result["top_matched_keywords"]),
            missing_keywords=", ".join(result["missing_keywords"]),
            suggestions="\n".join(result["suggested_bullets"]),
            resume_text_preview=result["resume_text_preview"],
            jd_text_preview=result["jd_text_preview"],
        )
        db.add(run)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.exception("Failed to save run: %s", e)
    finally:
        db.close()
