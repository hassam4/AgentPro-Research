import fitz  # PyMuPDF


def read_pdf(path: str) -> str:
    """Extract text from a PDF file."""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
