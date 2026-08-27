from customer_support_ai.services.knowledge_base_service import knowledge_service
from langchain_core.tools import tool


@tool
def retrieve_documents(query: str, intent: str, limit: int = 3):
    '''Searches the knowledge base for provided query based on its intent'''
    return knowledge_service.search(query=query, intent=intent, limit=limit)
