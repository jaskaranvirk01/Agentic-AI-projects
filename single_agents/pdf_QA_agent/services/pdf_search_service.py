from services.retriever_manager import retriever_manager


class PdfSearchService:
    def __init__(self):
        pass

    def _get_retriever(self):
        return retriever_manager.get_retriever()

    def search(self, user_query: str):
        retriever = self._get_retriever()
        if retriever is None:
            return 'No PDF has been loaded'

        return retriever.invoke(user_query)


pdf_search_service = PdfSearchService()
