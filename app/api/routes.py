from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.schemas.match import MatchResponse
from app.services.matcher import run_match
from app.db.crud import save_run

router = APIRouter(tags=["Matching"])

@router.post("/match", response_model=MatchResponse)
async def match_resume_to_jd(
    resume_pdf: UploadFile = File(...),
    job_description: str = Form(...),
    use_tfidf: bool = Form(True),
):
    if resume_pdf.content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Resume must be a PDF file.")

    if not job_description or len(job_description.strip()) < 50:
        raise HTTPException(status_code=400, detail="Job description is too short (min 50 chars).")

    result = await run_match(
        resume_pdf=resume_pdf,
        job_description=job_description,
        use_tfidf=use_tfidf,
    )

    save_run(result)
    return result
