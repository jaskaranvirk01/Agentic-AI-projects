from langchain.tools import tool
from services.pdf_reader_service import pdf_reader_service


@tool
def pdf_reader(file_path: str):
    """This tool reads the PDF file and prepares it for semantic search."""
    return pdf_reader_service.load_pdf(file_path)
