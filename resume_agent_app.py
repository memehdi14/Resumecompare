import streamlit as st
import os
import pdfplumber
from dotenv import load_dotenv
from Resume_Agent import parse_resume, evaluate_resumes_with_gpt

# Load environment variables
load_dotenv()

# Streamlit page settings
st.set_page_config(page_title="Resume Evaluation Agent", layout="centered")
st.title("Resume Evaluation Agent")

# --- App Info Section ---
st.markdown("""
Welcome to the **Resume Evaluation Agent**!  
This tool uses AI to evaluate how well a resume matches a job description using LangChain + Gemini.

---

### How to Use:
1. **Upload your resume** as a PDF.
2. **Paste or upload** the job description.
3. Click **Run Evaluation** to get an AI-generated rating and explanation.
""")

# --- Resume Upload ---
st.subheader("Step 1: Upload Your Resume")
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

# --- Job Description Upload ---
st.subheader("Step 2: Provide the Job Description")
col1, col2 = st.columns([4, 1])

with col1:
    jd_text = st.text_area("Paste Job Description (optional)", height=200)

with col2:
    jd_pdf = st.file_uploader("Or Upload JD (PDF)", type="pdf")

# Extract text from JD PDF if uploaded
if jd_pdf:
    with pdfplumber.open(jd_pdf) as pdf:
        jd_text = ""
        for page in pdf.pages:
            jd_text += page.extract_text()

# --- Run Evaluation Button ---
run_button = st.button("Run Evaluation")

if run_button:
    if not uploaded_resume:
        st.warning("Please upload a resume.")
    elif not jd_text.strip():
        st.warning("Please provide a job description (paste or upload).")
    else:
        # Save resume and process
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_resume.read())
        resume_text = parse_resume("temp_resume.pdf")

        # Evaluate
        results = evaluate_resumes_with_gpt([(resume_text, 0.95)], jd_text)

        # Show result
        st.header("📊 Evaluation Result")
        st.success("Resume evaluated successfully!")
        st.text_area("💬 GPT Feedback", results[0]["gpt_response"], height=300)

# --- Footer ---
st.markdown("---")
st.caption("Built with LangChain + Gemini | by Mehdi Namdar")
