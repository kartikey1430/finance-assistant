AI Tool Usage Log

API Agent (Stock Data)

Library: yfinance

Function: Pulls latest stock closing prices and calculates percentage change.

Example: Fetch TSM 2-day close → compute % change


Scraper Agent


Library: requests, dotenv

API: NewsData.io

Function: Retrieve recent business headlines in English.

Usage: get_market_headlines() returns top 5 headlines


Retriever Agent


Embedding: sentence-transformers/all-MiniLM-L6-v2

Vector Store: FAISS

LangChain Component: FAISS.from_documents()

Query: vector_db.similarity_search(user_query)


Analysis Agent


Technique: Rule-based sentiment analysis

Thresholds:
+1% → Positive
< -1% → Negative
Else → Neutral
Function: analyze_sentiment(change_percent)


Voice Agent


Speech Recognition: SpeechRecognition (Google STT)

Speech Output: pyttsx3

Pipeline:

Record voice from mic

Transcribe using Google Web API

Fetch stock data

Speak results aloud


Orchestrator


Location: orchestrator/orchestrator.py

Function: Pulls all agents together to:

Fetch data

Retrieve relevant info

Perform sentiment

Output structured results


Streamlit Frontend


Component: streamlit_app/app.py

Widgets:

Button to fetch stock data

Display of % change and sentiment

Live Output: Interactive sentiment dashboard