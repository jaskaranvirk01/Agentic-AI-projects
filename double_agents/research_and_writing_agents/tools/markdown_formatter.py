from langchain.tools import tool
from llm.client import markdown_llm
from langchain_core.prompts import ChatPromptTemplate

markdown_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a Markdown formatting assistant.

Convert the provided text into clean, well-structured Markdown.

Use headings, bullet points, numbered lists, tables, and code blocks whenever appropriate.

Do not change or add information.
Return only valid Markdown.
"""
    ),
    ("human", "{text}")
])

chain = markdown_prompt | markdown_llm


@tool
def markdown_formatter(text: str) -> str:
    """Format text into clean Markdown without changing its meaning."""
    return chain.invoke({"text": text}).content
