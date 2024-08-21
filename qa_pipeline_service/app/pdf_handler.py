from pdfminer.high_level import extract_text
from io import BytesIO

def extract_pdf_text(pdf_content: bytes) -> str:
    with BytesIO(pdf_content) as pdf_file:
        text = extract_text(pdf_file)
    return text
