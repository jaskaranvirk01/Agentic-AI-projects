from langchain.tools import tool
from services.pdf_search_service import pdf_search_service


@tool
def pdf_search(user_query: str):
    """Retrieves relevant information from the loaded PDF."""
    docs = pdf_search_service.search(user_query)

    if isinstance(docs, str):
        return docs

    return "\n".join(doc.page_content for doc in docs)
