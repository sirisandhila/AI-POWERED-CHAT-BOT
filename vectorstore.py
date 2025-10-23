from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
import os
from qa_chain import run_qa_chain

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-east1-gcp")
index = pinecone.Index("pdf-documents")
embedding = OpenAIEmbeddings()

def store_document_chunks(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    Pinecone.from_texts(chunks, embedding=embedding, index_name="pdf-documents")

def query_document(question: str):
    vectorstore = Pinecone(index, embedding.embed_query)
    docs = vectorstore.similarity_search(question, k=5)
    return run_qa_chain(question, docs)
