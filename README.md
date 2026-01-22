# JobFit AI – Resume vs Job Description Matching (ATS Scorer)

JobFit AI compares a Resume (PDF) with a Job Description and returns:
- Match score (%) using sentence-transformers embeddings + cosine similarity
- Optional TF-IDF baseline score (%)
- Top matched keywords (Top 10)
- Missing keywords (Top 10)
- Suggested improved resume bullets (3–5)
- Stores each run result in SQLite

---

## Project Structure

