import os
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Set path to documents
pdf_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "documents"))
if not os.path.exists(pdf_dir):
    raise FileNotFoundError(f"Directory not found: {pdf_dir}")

# Load all PDFs
loaders = [PyPDFLoader(os.path.join(pdf_dir, fn)) for fn in os.listdir(pdf_dir) if fn.endswith(".pdf")]
documents = []
for loader in loaders:
    documents.extend(loader.load())

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(documents=texts, embedding=embedding_model)

# Load your LLaMA model (update the path and parameters accordingly)
llm = LlamaCpp(
    model_path="C:/Users/AMOHA/PycharmProjects/VC_RAG/models/mistral-7b-instruct-v0.1.Q3_K_L.gguf",
    temperature=0.7,
    max_tokens=512,
    top_p=0.95,
    n_ctx=4096,
    n_threads=6,
    f16_kv=True,
    verbose=True,
)

# Create Retrieval QA chain
retriever = vectordb.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Sample query
query = "What is capital of India?"
response = qa.invoke({"query": query})

# Output
print("Answer:", response['result'])
