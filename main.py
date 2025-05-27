from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from data_ingestion.api_agent import get_asia_tech_data
from data_ingestion.scraper_agent import get_market_headlines
from agents.analysis_agent import analyze_sentiment
from agents.retriever_agent import load_sample_docs, build_vector_index, get_relevant_info

app = FastAPI(title="Finance Assistant API", version="1.0")

# Initialize retriever index
docs = load_sample_docs()
vector_db = build_vector_index(docs)

class WelcomeMessage(BaseModel):
    message: str

class QueryRequest(BaseModel):
    question: str

@app.get("/", response_model=WelcomeMessage)
def root():
    return {"message": "Welcome to the Finance Assistant API!"}

@app.get("/api-agent")
def get_stocks():
    try:
        data = get_asia_tech_data()
        for item in data:
            change = item.get("change_percent")
            if change is not None:
                item["sentiment"] = analyze_sentiment(change)
            else:
                item["sentiment"] = "unknown"
        return {"stocks": data}
    except Exception as e:
        return {"error": str(e)}

@app.get("/scraper-agent")
def get_headlines():
    try:
        headlines = get_market_headlines()
        return {"headlines": headlines}
    except Exception as e:
        return {"error": str(e)}

@app.post("/retriever-agent")
def retrieve_info(req: QueryRequest):
    response = get_relevant_info(req.question, vector_db)
    if not response or "couldn't find" in response.lower():
        return {"response": "Sorry, I couldn’t find relevant information. Could you please rephrase?"}
    return {"response": response}

@app.post("/analysis-agent")
def analyze(req: QueryRequest):
    try:
        change = float(req.question.strip('%'))
        sentiment = analyze_sentiment(change)
        return {"change": change, "sentiment": sentiment}
    except ValueError:
        return {"error": "Invalid input. Please enter a valid percentage like 2.5 or -1.3"}
