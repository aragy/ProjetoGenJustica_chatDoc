from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .pdf_handler import extract_pdf_text
from .text_splitter import split_text
from .vector_db import store_chunks, search_similar_chunks
from .qa_pipeline import get_answer

app = FastAPI()

class PDFResponse(BaseModel):
    status: str

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.post("/process_pdf/", response_model=PDFResponse)
async def process_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_pdf_text(content)
    chunks = split_text(text)
    store_chunks(chunks)
    return PDFResponse(status="PDF processed and chunks stored")

@app.post("/ask_question/", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    answer = get_answer(request.question)
    return AnswerResponse(answer=answer)
