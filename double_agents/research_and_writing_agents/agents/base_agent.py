from langchain_core.messages import SystemMessage,  ToolMessage
from langchain_mistralai import ChatMistralAI
import json
from abc import ABC, abstractmethod


class BaseAgent:

    def __init__(self, llm: ChatMistralAI, tools: list, system_prompt: str):
        self.llm = llm
        self.llm_with_tools = llm.bind_tools(tools)
        self.system_prompt = system_prompt
        self.messages = [SystemMessage(content=system_prompt)]

    @abstractmethod
    def invoke(self, input):
        pass

    def continue_conversation(self):
        response = self.llm_with_tools.invoke(self.messages)
        self.messages.append(response)
        return response

    def add_tool_message(self, tool_result, tool_call_id):

        if not isinstance(tool_result, str):
            tool_result = json.dumps(tool_result, indent=2, default=str)

        self.messages.append(
            ToolMessage(
                content=tool_result,
                tool_call_id=tool_call_id
            )
        )

    def reset(self):
        self.messages = [SystemMessage(content=self.system_prompt)]
