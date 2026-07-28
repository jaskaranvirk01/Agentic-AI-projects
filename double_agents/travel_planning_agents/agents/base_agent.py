from llm.client import ChatMistralAI
from langchain_core.messages import SystemMessage, ToolMessage, ToolCall
from typing import Any


class BaseAgent:
    def __init__(self, llm: ChatMistralAI, tools: list[Any], system_prompt: str):
        self.llm = llm
        self.llm_with_tools = self.llm.bind_tools(tools)
        self.system_message = system_prompt
        self.messages = [SystemMessage(content=self.system_message)]

    def continue_conversation(self):
        response = self.llm_with_tools.invoke(self.messages)

        self.messages.append(response)

        return response

    def add_tool_message(self, tool_result, tool_call: ToolCall):
        self.messages.append(ToolMessage(
            content=tool_result,
            tool_call_id=tool_call['id']
        ))

    def reset(self):
        self.messages = [SystemMessage(content=self.system_message)]
