from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

docs_path = "../data/documents"
index_path = "../data/faiss_index"

def load_and_split_pdfs():
    documents = []
    for filename in os.listdir(docs_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(docs_path, filename))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

def embed_and_store(docs):
    # 🆕 Use multilingual embedding model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    print("✅ Multilingual vector store created and saved.")

if __name__ == "__main__":
    chunks = load_and_split_pdfs()
    embed_and_store(chunks)
