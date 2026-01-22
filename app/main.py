from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logging import setup_logging
from app.api.routes import router as api_router
from app.db.database import init_db

setup_logging()

app = FastAPI(
    title="JobFit AI – ATS Scorer",
    version="1.0.0",
    description="Resume vs Job Description Matching using embeddings + TF-IDF baseline",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
