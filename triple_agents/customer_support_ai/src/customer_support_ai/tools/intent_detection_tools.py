from langchain_core.tools import tool
from customer_support_ai.llm.client import llm
from customer_support_ai.schemas.intent_detection_schemas import IntentOutput


@tool
def intent_detection_tool(messages) -> IntentOutput:
    '''Detects and categories query in terms of provided intents'''
    structured_llm = llm.with_structured_output(IntentOutput)
    return structured_llm.invoke(messages)
