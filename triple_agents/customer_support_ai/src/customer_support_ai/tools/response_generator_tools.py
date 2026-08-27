from langchain_core.tools import tool
from customer_support_ai.llm.client import llm


@tool
def response_generator_tool(messages) -> str:
    '''Invokes the llm to generate final response for the given messsages data'''
    response = llm.invoke(messages)
    return response.content
