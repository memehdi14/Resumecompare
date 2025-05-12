import streamlit as st
import os
from dotenv import load_dotenv
import pdfplumber
from Resume_Agent import parse_resume, evaluate_resumes_with_gpt

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

st.title("Resume Evaluation Agent")

# Upload resume
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

# Upload job description PDF
st.markdown("### Job Description")
jd_col1, jd_col2 = st.columns([4, 1])

with jd_col1:
    jd_text = st.text_area("Paste Job Description Here (optional)", height=200)

with jd_col2:
    jd_pdf = st.file_uploader("Upload JD (PDF)", type="pdf", key="jd")

# Extract JD text if a JD PDF is uploaded
if jd_pdf:
    with pdfplumber.open(jd_pdf) as pdf:
        jd_text = ""
        for page in pdf.pages:
            jd_text += page.extract_text()

# Evaluation logic
if uploaded_resume and jd_text.strip():
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_resume.read())
    resume_text = parse_resume("temp_resume.pdf")

    # You can tweak the similarity score as needed or remove it
    results = evaluate_resumes_with_gpt([(resume_text, 0.95)], jd_text)

    st.subheader("GPT Evaluation (with Rating):")
    st.text_area("GPT Output", results[0]["gpt_response"], height=300)
