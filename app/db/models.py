from sqlalchemy import Column, Integer, Float, Text, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class MatchRun(Base):
    __tablename__ = "match_runs"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    score_embeddings = Column(Float, nullable=False)
    score_tfidf = Column(Float, nullable=True)

    matched_keywords = Column(Text, nullable=False)
    missing_keywords = Column(Text, nullable=False)

    suggestions = Column(Text, nullable=False)

    resume_text_preview = Column(Text, nullable=False)
    jd_text_preview = Column(Text, nullable=False)
