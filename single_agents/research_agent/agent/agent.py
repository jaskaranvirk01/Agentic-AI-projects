from tools.calculator import calculator
from tools.web_search import web_search
from llm.client import llm
from agent.prompt import SYSTEM_PROMPT
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage,  SystemMessage


class Agent:
    def __init__(self, llm: ChatMistralAI, tools: list[tool]):
        self.llm = llm
        self.llm_with_tools = self.llm.bind_tools(tools)
        self.messages = [SystemMessage(content=SYSTEM_PROMPT)]

    def invoke(self, user_query: str):
        self.messages.append(HumanMessage(content=user_query))

        response = self.llm_with_tools.invoke(self.messages)

        self.messages.append(response)

        return response

    def continue_conversation(self):
        response = self.llm_with_tools.invoke(self.messages)
        self.messages.append(response)
        return response

    def add_tool_message(self, tool_result, tool_call_id):
        self.messages.append(
            ToolMessage(
                content=tool_result,
                tool_call_id=tool_call_id
            )
        )

    def reset(self):
        self.messages = [SystemMessage(content=SYSTEM_PROMPT)]


agent = Agent(llm=llm, tools=[web_search, calculator])
