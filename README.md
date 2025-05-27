# 🧠 Finance Assistant – Multi-Agent AI System

A modular, multi-agent finance assistant that fetches, analyzes, and presents real-time financial data with voice interaction support and an intuitive UI.

## 🚀 Features

- 📊 **API Agent**: Fetches Asia tech stock data using `yfinance`
- 🗞️ **Scraper Agent**: Retrieves market headlines from financial sources
- 🧠 **Analysis Agent**: Performs sentiment analysis using `TextBlob`
- 📚 **Retriever Agent**: Context-aware Q&A using vector index and LangChain
- 🎙️ **Voice Agent**: Supports voice-based queries via STT + TTS
- 🧩 **Streamlit UI**: Real-time visualization with dark/light theme toggle
- 🌐 **FastAPI**: Backend orchestration of all agents

---

## 🗂️ Directory Structure

finance-assistant/
│
├── agents/
│ ├── api_agent.py
│ ├── analysis_agent.py
│ ├── language_agent.py
│ ├── retriever_agent.py
│ └── voice_agent.py
│
├── data_ingestion/
│ ├── api_agent.py
│ └── scraper_agent.py
│
├── orchestrator/
│ └── orchestrator.py
│
├── streamlit_app/
│ └── app.py
│
├── main.py
├── ai_tool_usage.md
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/kartikey1430/finance-assistant.git
   cd finance-assistant

2. **Create Virtual Environment**
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Mac/Linux

3. **Install Dependencies**
    pip install -r requirements.txt


How to Run
1. Start FastAPI Server
    python -m uvicorn main:app --reload
    Visit: http://127.0.0.1:8000/docs

2. Launch Streamlit UI
    streamlit run streamlit_app/app.py

3. Use Voice Agent
    python agents/voice_agent.py


Tech Stack
    FastAPI + Uvicorn
    Streamlit for dashboard UI
    yfinance for stock data
    TextBlob for sentiment
    LangChain + FAISS for retrieval
    SpeechRecognition + gTTS for voice I/O

Sample API Endpoints
    GET /api-agent → Tech stock sentiment
    GET /scraper-agent → Market headlines
    POST /retriever-agent → Ask finance-related questions
    POST /analysis-agent → Analyze % change sentiment

Author
    Kartikey Agrawal
    https://www.linkedin.com/in/kartikey-agrawal02

Status
    Completed – All agents and interfaces tested & functional.

---