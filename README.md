# CompareResume

*CompareResume* is an AI-powered resume evaluation tool that helps job seekers assess how well their resume aligns with a specific job description. Built using Streamlit and Google's Gemini AI via LangChain, it provides a match score, strengths, and improvement areas — all in seconds.

[Live Demo](https://compareresume.streamlit.app)  
[GitHub Repo](https://github.com/memehdi14/compareresume)

---

## Features

- Upload resume in PDF format
- Paste or upload a job description (PDF optional)
- Extracts content from PDFs using pdfplumber
- Evaluates resumes using Gemini 1.5 Flash via LangChain
- Returns:
  - A match score (out of 10)
  - Strengths
  - Suggestions for improvement

---

## Tech Stack

- *Frontend*: Streamlit
- *AI Model*: Gemini 1.5 Flash (Google Generative AI)
- *Embeddings*: LangChain + ChromaDB
- *Text Extraction*: pdfplumber
- *Environment Management*: python-dotenv

---

## Getting Started

1. Clone the Repo

```bash
git clone https://github.com/memehdi14/compareresume.git
cd compareresume
```
2. Create Virtual Environment
```
python3.12 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install protobuf==3.20.3 --no-cache-dir
```
---

## Environment Setup

Create a .env file in the root directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

---

Run the App
```
streamlit run resume_agent_app.py
```
Open http://localhost:XXXX in your browser.


---

## Project Structure
```
compareresume/
├── resume_agent_app.py       # Streamlit frontend
├── Resume_Agent.py           # Parsing, vector search & evaluation
├── requirements.txt
├── .env                      # API key (never push to GitHub)
└── README.md
```

---

Sample Output
```
Score: 8.2 / 10

Strengths: Relevant experience, key skill matches

Suggestions: Includes specific tools mentioned in JD
```


---
#### About me:-
```
I’m Mehdi Namdar — passionate about AI, automation, and building meaningful tools.
If you found this project useful or have ideas to improve it, feel free to connect or contribute.
Let’s build something better together!
```
[GitHub](https://github.com/memehdi14) [LinkedIn](https://in.linkedin.com/in/mohammad-mehdi-namdar-042609327) [Email](Namdar.medhi14@gmail.com) [Instagram](instagram.com/MehXBot)
---
#### License

MIT License — free for personal and commercial use. Credit appreciated

---
#### Contribute

Open to ideas, pull requests, and collaborations. 
Feel free to fork and enhance!
Credit would be appreciated but not neccesite.......
---
