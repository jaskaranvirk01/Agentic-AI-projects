from customer_support_ai.tools.knowledge_base_tools import retrieve_documents


class KnowledgeBaseAgent:
    def __init__(self):
        pass

    def get_documents(self, query: str, intent: str, limit: int = 3) -> list:
        return retrieve_documents.invoke({
            'query': query,
            'intent': intent,
            'limit': limit
        })


knowledge_base_agent = KnowledgeBaseAgent()
