# rag_wrapper.py

from semantic_search import qa

def query_semantic_search(query: str) -> str:
    response = qa.invoke({"query": query})
    return response['result']