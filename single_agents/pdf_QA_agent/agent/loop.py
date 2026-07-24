from agent.agent import agent
from tools.doc_reader import pdf_reader
from tools.doc_search import pdf_search

tools = {
    'pdf_reader': pdf_reader,
    'pdf_search': pdf_search
}


def agent_loop(user_query):
    agent.reset()
    result = agent.invoke(user_query)
    while True:

        if not result.tool_calls:
            print(result.content)
            break

        for tool_call in result.tool_calls:
            tool_name = tool_call['name']
            print(f'Name : {tool_name} ')
            print(f'Arguments: {tool_call['args']} ')

            confirm = input("want to use ? reply with (y/n) : ")

            if confirm.lower() != 'y':
                tool_result = (
                    "Tool execution denied by the user. "
                    "Answer without using this tool if possible."
                )

            else:
                try:
                    tool_result = tools[tool_name].invoke(tool_call['args'])
                except Exception as e:
                    tool_result = f'an Error occured : {e}'

            agent.add_tool_message(tool_result, tool_call['id'])
        result = agent.continue_conversation()
