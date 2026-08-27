from customer_support_ai.tools.response_generator_tools import response_generator_tool
from langchain_core.messages import SystemMessage, HumanMessage
from customer_support_ai.prompts.response_generator_prompts import SYSTEM_PROMPT


class ResponseGeneratorAgent:
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT

    def generate_response(self, query: str, intent: str, articles: list) -> str:
        messages = [SystemMessage(content=self.system_prompt), HumanMessage(content=f'''
Custome query : 
{query}

intent:
{intent}

articles:
{articles}
''')]
        return response_generator_tool.invoke({
            'messages': messages
        })


response_generator_agent = ResponseGeneratorAgent()
