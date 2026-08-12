from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatMistralAI(model='ministral-3b-2512', temperature=0)
