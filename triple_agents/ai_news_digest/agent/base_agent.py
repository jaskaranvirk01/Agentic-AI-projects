from llm.client import ChatMistralAI
from langchain_core.messages import SystemMessage, ToolCall, ToolMessage
from typing import Any
from llm.wrapper import invoke_llm


class BaseAgent:
    def __init__(self, llm: ChatMistralAI, tools: list[Any], system_prompt: str):
        self.llm = llm
        self.tools = tools
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.system_prompt = system_prompt
        self.messages = [SystemMessage(content=self.system_prompt)]

    def continue_conversation(self):
        response = invoke_llm(model=self.llm_with_tools, prompt=self.messages)
        self.messages.append(response)
        return response

    def add_tool_message(self, tool_result: str, tool_call: ToolCall):
        self.messages.append(ToolMessage(
            content=tool_result, tool_call_id=tool_call['id']
        ))

    def reset(self):
        self.messages = [SystemMessage(content=self.system_prompt)]
