from llm.client import llm
from langchain_mistralai import ChatMistralAI
from tools.email_writer import create_gmail_draft
from tools.add_meeting import create_meeting
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from agent.prompt import SYSTEM_PROMPT
tools = [create_gmail_draft, create_meeting]


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

    def add_tool_message(self, tool_result, tool_call_id):
        self.messages.append(ToolMessage(
            content=str(tool_result), tool_call_id=tool_call_id))

    def continue_conversation(self):
        response = self.llm_with_tools.invoke(self.messages)
        self.messages.append(response)
        return response

    def reset(self):
        self.messages = [SystemMessage(content=SYSTEM_PROMPT)]


automation_agent = Agent(llm, tools)
