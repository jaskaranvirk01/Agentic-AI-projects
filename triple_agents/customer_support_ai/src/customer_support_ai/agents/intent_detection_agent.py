from customer_support_ai.tools.intent_detection_tools import intent_detection_tool
from customer_support_ai.schemas.intent_detection_schemas import IntentOutput
from customer_support_ai.prompts.intent_detection_prompts import SYSTEM_PROMPT
from langchain_core.messages import SystemMessage, HumanMessage


class IntentDetectionAgent:
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT

    def detect_intent(self, query: str) -> IntentOutput:
        messages = [SystemMessage(content=self.system_prompt), HumanMessage(
            content=f'Customer query:{query}')]

        return intent_detection_tool.invoke({'messages': messages})


intent_detection_agent = IntentDetectionAgent()
