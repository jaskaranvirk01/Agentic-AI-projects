from tools.csv_reader import read_csv
from tools.calculator import calculator
from agent.agent import finance_agent
tools = {
    'calculator': calculator,
    'read_csv': read_csv
}


def agent_loop(user_query):
    finance_agent.reset()
    result = finance_agent.invoke(user_query)

    while True:

        if not result.tool_calls:
            print(result.content)
            return result.content

        for tool_call in result.tool_calls:
            tool_name = tool_call['name']
            print(f'Do you want to use : {tool_name}')
            print(f'arguments: {tool_call['args']}')

            confirm = input("Enable it ? : (y/n)")

            if confirm.lower() != 'y':
                tool_result = ("Tool execution denied by the user. "
                               "Answer without using this tool if possible.")
            else:
                try:
                    tool_result = tools[tool_name].invoke(tool_call['args'])
                except Exception as e:
                    tool_result = f'Error while executing tool : {e}'

            finance_agent.add_tool_message(
                tool_result=tool_result, tool_call_id=tool_call['id'])
        result = finance_agent.continue_conversation()
