
class RetrieverManager:
    def __init__(self):
        self.retriever = None

    def set_retriever(self, retriever):
        self.retriever = retriever

    def get_retriever(self):
        return self.retriever

    def has_retriever(self):
        return self.retriever != None


retriever_manager = RetrieverManager()
