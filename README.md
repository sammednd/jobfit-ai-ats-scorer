# JobFit AI — ATS Resume Scorer (Resume vs Job Description)

JobFit AI is a resume-to-job-description matching tool that generates an **ATS-style match score**, highlights **matched/missing keywords**, and suggests **resume bullet improvements** to better align your resume with a target role.

It uses **semantic similarity (Sentence Transformers + cosine similarity)** and can optionally compute a **TF-IDF baseline score**.

---

## ✨ Features

- ✅ **ATS Match Score (%)** using sentence embeddings + cosine similarity  
- ✅ **TF-IDF Similarity Score** (baseline comparison)  
- ✅ **Matched Keywords** found in both resume and job description  
- ✅ **Missing Keywords** from the job description not found in the resume  
- ✅ **AI Suggestions** (3–5 improved resume bullets)  
- ✅ **SQLite Logging** to store scoring runs  
- ✅ **Frontend + Backend structure**  
- ✅ **Docker support** for easy setup  

---

## 🧱 Project Structure

```text
jobfit-ai-ats-scorer/
│
├── app/        # Backend app logic (scoring, API, services)
├── frontend/   # Frontend UI
├── utils/      # Helper functions (text cleaning, extraction, etc.)
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md



---

## ⚙️ Requirements

- Python 3.9+ recommended  
- pip / virtualenv (or conda)  
- (Optional) Docker + Docker Compose  

---

## 🚀 Setup (Local)

### 1) Clone the repo

```bash
git clone https://github.com/sammednd/jobfit-ai-ats-scorer.git
cd jobfit-ai-ats-scorer

2) Create & activate a virtual environment

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate


Windows

python -m venv .venv
.venv\Scripts\activate

3) Install dependencies
pip install -r requirements.txt

4) Configure environment variables

Copy the example file:

cp .env.example .env


Update .env with any required keys/settings (if applicable).

▶️ Running the App

The project includes both backend + frontend. Depending on the repo implementation,
you may run backend only or full stack.

Backend (example)

If the backend is FastAPI/Flask-based, typical run commands look like:

python -m app.main


or

uvicorn app.main:app --reload


If the repo has a specific entrypoint script, run that instead.

🐳 Run with Docker
Build and run
docker-compose up --build


Stop containers:

docker-compose down

🧠 How Scoring Works (High Level)

Text extraction from resume + job description

Cleaning & normalization

Embedding generation using Sentence Transformers

Cosine similarity between resume and JD embeddings → Match Score

Keyword overlap analysis:

Matched keywords

Missing keywords

Optional TF-IDF similarity score

Results saved to SQLite for tracking

📌 Example Output

A typical result may include:

Match Score: 78%

TF-IDF Score: 0.61

Matched Keywords: ["Python", "FastAPI", "Docker", ...]

Missing Keywords: ["Kubernetes", "CI/CD", ...]

Suggested Bullets:

“Built scalable APIs using FastAPI and deployed using Docker...”

“Improved performance by optimizing SQL queries...”

“Implemented CI/CD pipelines to automate testing and deployment...”

🗃️ Logging (SQLite)

Each scoring run can be logged into an SQLite database for later reference.

Example fields commonly stored:

timestamp

job title (optional)

match score

matched keywords

missing keywords

🧪 Testing

If tests exist in the repo:

pytest


(If there are no tests yet, feel free to add them under tests/.)

🔐 Notes / Limitations

This tool provides an approximate match score, not a real ATS system score.

Keyword matching depends on text extraction quality and formatting.

Results improve when resumes are cleanly formatted and job descriptions are detailed.

🛣️ Roadmap (Suggested Improvements)

 Add PDF/DOCX resume parsing support (if not already present)

 Add API docs (Swagger/OpenAPI)

 Add better keyword extraction (NER / skill taxonomy)

 Add multi-role comparison (one resume vs many jobs)

 Add resume formatting feedback (ATS readability checks)

 Add unit tests + CI pipeline

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a feature branch

Commit changes

Open a Pull Request

📄 License

Add your license here (MIT/Apache-2.0/etc).
If no license is included, GitHub defaults to “All Rights Reserved”.

⭐ Acknowledgements

Sentence Transformers for semantic similarity embeddings

TF-IDF baseline similarity methods

Open-source community tools powering resume analysis
