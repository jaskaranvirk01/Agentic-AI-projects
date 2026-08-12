from langchain_core.messages import AIMessage


def run_agent(agent, input_data, require_confirmation: bool = True) -> AIMessage:
    """
    Execute an agent until it produces a final response.
    """

    response = agent.invoke(input_data)

    tool_map = {
        tool.name: tool
        for tool in agent.tools
    }

    while response.tool_calls:

        print("\n=== Tool Calls ===")
        for index, tool_call in enumerate(response.tool_calls, start=1):
            print(f"{index}. {tool_call['name']}")
            print(f"   Args: {tool_call['args']}")

        if require_confirmation:
            confirm = input("\nExecute these tool(s)? (y/n): ").strip().lower()

            if confirm != "y":
                print("Tool execution cancelled.")
                return response

        for tool_call in response.tool_calls:

            tool = tool_map[tool_call["name"]]

            print(f"\nExecuting {tool.name}...")

            tool_result = tool.invoke(tool_call["args"])

            agent.add_tool_message(
                tool_result=str(tool_result),
                tool_call=tool_call,
            )

        response = agent.continue_conversation()

    return response
