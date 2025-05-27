# 📈 Asia Tech Stock Sentiment Assistant

An AI-powered multi-agent assistant that fetches, analyzes, and vocalizes stock sentiment data for major Asian tech stocks using Yahoo Finance APIs. Built with Python, LangChain, FAISS, Streamlit, and speech libraries.

---

## 🔧 Features

- 🔍 Scrapes live market news headlines
- 📉 Fetches real-time stock prices (TSM, Samsung, etc.)
- 🤖 Classifies stock sentiment (positive, negative, neutral)
- 🧠 Embeds and retrieves relevant news using FAISS + Langchain
- 🗣️ Voice command interface to query and speak results
- 🌐 Streamlit frontend for an interactive UI

---

## 🗂️ Project Structure

finance-assistant/
├── agents/
│ ├── analysis_agent.py
│ ├── retriever_agent.py
│ ├── voice_agent.py
├── data_ingestion/
│ ├── api_agent.py
│ ├── scraper_agent.py
├── orchestrator/
│ ├── orchestrator.py
├── streamlit_app/
│ └── app.py
├── .env
├── requirements.txt
├── README.md
└── docs/ai_tool_usage.md


---

## 🚀 How to Run the Project

### Step 1: Install Requirements

```bash
pip install -r requirements.txt

Step 2: Set Your API Key

Create a .env file with this inside:

NEWSDATA_API_KEY=pub_e0e66da5a1984c6b8a06d0bd67d6d971

Step 3: Run Components

| Component       | Command                                  |
| --------------- | ---------------------------------------- |
| API Agent       | `python data_ingestion/api_agent.py`     |
| Scraper Agent   | `python data_ingestion/scraper_agent.py` |
| Retriever Agent | `python agents/retriever_agent.py`       |
| Analysis Agent  | `python agents/analysis_agent.py`        |
| Voice Agent     | `python -m agents.voice_agent`           |
| Orchestrator    | `python orchestrator/orchestrator.py`    |
| Streamlit App   | `streamlit run streamlit_app/app.py`     |
| FastAPI Backend | `uvicorn main:app --reload`              |

📊 Sample Output

TSM: -2.12% → Sentiment: Negative
005930.KQ: +1.35% → Sentiment: Positive

Tools & Libraries

LangChain + HuggingFace
FAISS vector search
Streamlit
yFinance (Yahoo Finance)
pyttsx3 (Text-to-Speech)
SpeechRecognition (Voice input)
NewsData.io (Headline API)

Author

Kartikey Agrawal
B.Tech CSE, VIT Vellore
https://www.linkedin.com/in/kartikey-agrawal02