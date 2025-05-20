import streamlit as st
import os
import pdfplumber
from dotenv import load_dotenv
from Resume_Agent import parse_resume, evaluate_resumes_with_gpt

# Load environment variables
load_dotenv()


# Streamlit page settings
st.set_page_config(page_title="ResumeCompare", layout="centered")
st.markdown("<h1 style='text-align: center; color:green;'>🛡ResumeCompare</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>AI-Powered Resume vs Job Description Comparison</p>", unsafe_allow_html=True)
st.markdown("---")

# How to Use
st.markdown("""How to Use?
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

jd_text_input = ""
with col1:
    jd_text_input = st.text_area("Paste Job Description (optional)", height=200)

jd_pdf_text = ""
with col2:
    jd_pdf = st.file_uploader("Or Upload JD (PDF)", type="pdf")
    if jd_pdf:
        try:
            with pdfplumber.open(jd_pdf) as pdf:
                for page in pdf.pages:
                    jd_pdf_text += page.extract_text() or ""
        except Exception as e:
            st.error(f"Error reading JD PDF: {e}")

# Use either text area nput or PDF text
final_jd_text = jd_pdf_text if jd_pdf_text.strip() else jd_text_input

# --- Run Evaluation Button ---
run_button = st.button("Run Evaluation")

if run_button:
    if not uploaded_resume:
        st.warning("Please upload a resume.")
    elif not final_jd_text.strip():
        st.warning("⚠Please provide a job description (paste or upload).")
    else:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_resume.read())

        resume_text = parse_resume("temp_resume.pdf")
        results = evaluate_resumes_with_gpt([(resume_text, 0.95)], final_jd_text)

        # Display Results
        st.header(" Evaluation Result")
        st.success(" Resume evaluated successfully!")
        st.text_area("GPT Feedback", results[0]["gpt_response"], height=300)

# --- Footer ---
st.markdown("---")
st.caption("Demo| Built with LangChain + Gemini | by Mehdi Namdar")
