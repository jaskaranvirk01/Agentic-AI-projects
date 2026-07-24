from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_mistralai.embeddings import MistralAIEmbeddings
from services.retriever_manager import retriever_manager


class PdfReaderService:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter()
        self.embeddings = MistralAIEmbeddings()

    def _load_document(self, file_path: str):
        loader = PyPDFLoader(file_path)
        return loader.load()

    def _split_document(self, documents):
        return self.text_splitter.split_documents(documents)

    def _create_vector_store(self, chunks):
        vector_store = FAISS.from_documents(
            chunks,
            self.embeddings
        )
        return vector_store

    def _create_retriever(self, vector_store):
        return vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 4
            }
        )

    def load_pdf(self, file_path: str):
        documents = self._load_document(file_path)
        chunks = self._split_document(documents)
        vector_store = self._create_vector_store(chunks)
        retriever = self._create_retriever(vector_store)

        retriever_manager.set_retriever(retriever)

        return "PDF loaded successfully."


pdf_reader_service = PdfReaderService()
