from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf_handler import extract_text_from_pdf
from vectorstore import store_document_chunks, query_document

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    store_document_chunks(text)
    return {"message": "Document uploaded and processed."}

@app.post("/ask/")
async def ask_question(query: dict):
    question = query.get("question")
    answer = query_document(question)
    return {"answer": answer}
