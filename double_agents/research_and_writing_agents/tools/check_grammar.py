from langchain.tools import tool
from llm.client import grammar_llm


from langchain_core.prompts import ChatPromptTemplate

grammar_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a grammar correction assistant.
Correct grammar, spelling, punctuation, and sentence structure.
Do not change the meaning.
Return only the corrected text."""
    ),
    ("human", "{text}")
])

chain = grammar_prompt | grammar_llm


@tool
def check_grammar(text: str) -> str:
    """
     Correct grammar, spelling, punctuation, and sentence structure
    while preserving the original meaning of the text.
    """

    return chain.invoke({'text': text}).content
