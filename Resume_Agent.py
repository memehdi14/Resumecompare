import os
import pdfplumber
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def parse_resume(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        resume_text = ""
        for page in pdf.pages:
            resume_text += page.extract_text()
    return resume_text

def create_embeddings(resume_texts):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return Chroma.from_texts(resume_texts, embeddings)
def evaluate_resumes_with_gpt(resume_texts_with_scores, job_description):
    model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0)
    results = []

    for resume_text, similarity_score in resume_texts_with_scores:
        chain = load_qa_chain(model, chain_type="stuff")
        gpt_response = chain.run(input_documents=[], question=f"""
            Evaluate the following resume against the job description.
            Give a rating out of 10 for how well the resume fits the job, followed by a short explanation.

            Job Description:
            {job_description}

            Resume:
            {resume_text}
        """)

        results.append({
            "resume_text": resume_text,
            "similarity_score": similarity_score,
            "gpt_response": gpt_response
        })

    return results
