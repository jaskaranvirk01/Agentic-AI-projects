from agent.agent import agent
from langchain_core.messages import ToolMessage
from tools.web_search import web_search
from tools.calculator import calculator
# from rich import print
tools = {
    "web_search": web_search,
    "calculator": calculator
}


def agent_loop(user_query: str):
    agent.reset()
    result = agent.invoke(user_query)
    while True:

        if not result.tool_calls:
            print("\n[bold green]Final Answer[/bold green]\n")
            print(result.content)
            print("\n" + "=" * 60)

            break

        for tool_call in result.tool_calls:
            tool_name = tool_call['name']

            print("\n[bold yellow]Tool Request[/bold yellow]")
            print(f"Tool : {tool_name}")
            print(f"Arguments : {tool_call['args']}")

            confirm = input("\nApprove tool? (y/n): ")

            if confirm.lower() != 'y':
                tool_result = (
                    "Tool execution denied by the user. "
                    "Answer without using this tool if possible."
                )

            else:

                try:
                    tool_result = tools[tool_name].invoke(tool_call['args'])
                except Exception as e:
                    tool_result = f"Tool execution failed.\nError: {e}"

            agent.add_tool_message(tool_result, tool_call['id'])
        result = agent.continue_conversation()
