from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.tools import tool

from schema.resume_analyzer import ReadPdfResponse


@tool
def read_pdf(file_name: str) -> ReadPdfResponse:
    """Load a resume PDF and return its extracted raw text."""

    pdf_path = Path(__file__).parent.parent / "data" / file_name

    if not pdf_path.exists():
        raise FileNotFoundError(f"Resume '{file_name}' not found.")

    loader = PyMuPDFLoader(file_path=str(pdf_path))
    documents = loader.load()

    resume_text = "\n".join(doc.page_content for doc in documents)

    return ReadPdfResponse(raw_text=resume_text)
