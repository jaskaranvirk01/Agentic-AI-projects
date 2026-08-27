from langchain_google_genai import ChatGoogleGenerativeAI
from stock_research.config.settings import settings


llm = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash',
    temperature=0.4,
    api_key=settings.google_api_key
)
