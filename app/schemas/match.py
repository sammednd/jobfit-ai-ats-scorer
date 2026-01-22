from pydantic import BaseModel, Field
from typing import List, Optional

class MatchResponse(BaseModel):
    match_score_embeddings: float = Field(..., ge=0, le=100)
    match_score_tfidf: Optional[float] = Field(None, ge=0, le=100)

    top_matched_keywords: List[str]
    missing_keywords: List[str]

    suggested_bullets: List[str]

    resume_text_preview: str
    jd_text_preview: str
