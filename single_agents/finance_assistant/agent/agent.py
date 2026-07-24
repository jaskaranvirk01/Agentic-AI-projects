from llm.client import llm
from langchain.tools import tool
from langchain_mistralai import ChatMistralAI
from tools.calculator import calculator
from tools.csv_reader import read_csv
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from agent.prompt import SYSTEM_PROMPT
tools = [
    calculator,
    read_csv
]


class FinanceAgent:
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


finance_agent = FinanceAgent(llm=llm, tools=tools)
