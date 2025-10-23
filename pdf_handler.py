from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf = PdfReader(io.BytesIO(file_bytes))
    return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
