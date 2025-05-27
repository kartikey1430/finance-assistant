import os
import pickle
from typing import List
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import FakeEmbeddings

# Sample documents for simulation
SAMPLE_DOCS = [
    "The stock market showed strong growth in the technology sector.",
    "Investors are cautious due to global inflation fears.",
    "TSMC's quarterly earnings beat expectations.",
    "Samsung's new chip boosts mobile performance by 25%.",
    "The Reserve Bank of India kept the repo rate unchanged."
]

def load_sample_docs() -> List[str]:
    return SAMPLE_DOCS

def build_vector_index(docs: List[str]):
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.create_documents(docs)
    embeddings = FakeEmbeddings(size=32)
    vector_db = FAISS.from_documents(texts, embeddings)
    return vector_db

def get_relevant_info(query: str, vector_db) -> str:
    results = vector_db.similarity_search(query, k=2)
    return "\n".join([res.page_content for res in results])
