from agent.agent import automation_agent
from tools.email_writer import create_gmail_draft
from tools.add_meeting import create_meeting
tools = {
    'create_gmail_draft': create_gmail_draft,
    'create_meeting': create_meeting
}


def agent_loop(user_query: str):
    result = automation_agent.invoke(user_query)
    while True:
        if not result.tool_calls:
            print(result.content)
            return

        for tool_call in result.tool_calls:
            tool_name = tool_call['name']
            print(f'Name : {tool_name}')
            print(f"Args : {tool_call['args']}")

            confirm = input(
                'Do you want to use this tool ? reply with (y/n) : ')

            if confirm.lower() != 'y':
                tool_result = ('The tool usage was declined by the user.')
            else:
                try:
                    tool_result = tools[tool_name].invoke(tool_call['args'])
                except Exception as e:
                    tool_result = f'Error while using the tool : {e}'

            automation_agent.add_tool_message(tool_result, tool_call['id'])

        result = automation_agent.continue_conversation()
