from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(model='mistral-small-2506', temperature=0)
grammar_llm = ChatMistralAI(model='mistral-small-2506', temperature=0)
markdown_llm = ChatMistralAI(model='mistral-small-2506', temperature=0)
