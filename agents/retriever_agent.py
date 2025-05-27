from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

# Use HuggingFaceEmbeddings wrapper for LangChain
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vector_index(docs: list[str]):
    documents = [Document(page_content=text) for text in docs]
    db = FAISS.from_documents(documents, embedding)
    return db

def search_similar_docs(db, query: str, k=3):
    results = db.similarity_search(query, k=k)
    return [doc.page_content for doc in results]

# Test
if __name__ == "__main__":
    sample_docs = [
        "Gold price prediction for May 26, 2025: Should you buy or sell?",
        "Monsoon rains arrive early in Kerala",
        "JSW Steel Q4 result: Margin expansion, steady growth",
        "Zeppto CEO accused of targeting rival firm",
        "Stock market opens lower as yields climb"
    ]

    vector_db = build_vector_index(sample_docs)
    query = "tech stock performance in Asia"
    similar = search_similar_docs(vector_db, query)

    print("🔍 Similar Results:")
    for line in similar:
        print("•", line)
