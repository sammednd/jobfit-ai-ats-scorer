import streamlit as st
import requests

API_URL = st.secrets.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="JobFit AI – ATS Scorer", layout="centered")

st.title("JobFit AI – Resume vs Job Description Matching")
st.caption("Upload a resume PDF + paste a job description to get ATS-style match results.")

resume_pdf = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=220)

use_tfidf = st.checkbox("Also compute TF-IDF baseline score", value=True)

if st.button("Score Match"):
    if resume_pdf is None:
        st.error("Please upload a resume PDF.")
        st.stop()

    if not job_description or len(job_description.strip()) < 50:
        st.error("Job description is too short (min 50 characters).")
        st.stop()

    files = {"resume_pdf": (resume_pdf.name, resume_pdf.getvalue(), "application/pdf")}
    data = {"job_description": job_description, "use_tfidf": str(use_tfidf).lower()}

    with st.spinner("Scoring..."):
        r = requests.post(f"{API_URL}/api/match", files=files, data=data, timeout=120)

    if r.status_code != 200:
        st.error(f"Request failed: {r.status_code} - {r.text}")
        st.stop()

    res = r.json()

    st.subheader("Match Score")
    st.metric("Embeddings Score", f"{res['match_score_embeddings']}%")

    if res.get("match_score_tfidf") is not None:
        st.metric("TF-IDF Score", f"{res['match_score_tfidf']}%")

    st.subheader("Top Matched Keywords")
    st.write(", ".join(res["top_matched_keywords"]))

    st.subheader("Missing Keywords")
    st.write(", ".join(res["missing_keywords"]))

    st.subheader("Suggested Improved Resume Bullets")
    for b in res["suggested_bullets"]:
        st.write(f"- {b}")

    with st.expander("Text Preview (Debug)"):
        st.write("Resume Preview:")
        st.code(res["resume_text_preview"])
        st.write("JD Preview:")
        st.code(res["jd_text_preview"])
