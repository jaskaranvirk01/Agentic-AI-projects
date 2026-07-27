from agents.research_agent import research_agent
from agents.writer_agent import writer_agent
from tools.web_search import web_search
from tools.calculator import calculator
from tools.check_grammar import check_grammar
from tools.markdown_formatter import markdown_formatter
from schemas.research_output import ResearchOutput
from schemas.writer_output import WriterOutput
tool_registry = {
    'web_search': web_search,
    'calculator': calculator,
    'check_grammar': check_grammar,
    'markdown_formatter': markdown_formatter
}


def execute_tool_loop(agent, tool_registry, result):

    while result.tool_calls:

        for tool_call in result.tool_calls:

            tool_name = tool_call["name"]

            print(f"Tool Name : {tool_name}")
            print(f"Arguments : {tool_call['args']}")

            confirm = input("Approve to use this tool (y/n) : ")

            if confirm.lower() != "y":
                tool_result = (
                    "The user denied permission to execute this tool. "
                    "Answer without using it."
                )
            else:
                try:
                    tool_result = tool_registry[tool_name].invoke(
                        tool_call["args"])
                except Exception as e:
                    tool_result = f"Error: {e}"

            agent.add_tool_message(
                tool_result=tool_result,
                tool_call_id=tool_call["id"]
            )

        result = agent.continue_conversation()

    return result


def research_agent_loop(user_query: str):

    result = research_agent.invoke(user_query)

    result = execute_tool_loop(
        research_agent,
        tool_registry,
        result
    )

    research_output = ResearchOutput(
        user_query=user_query,
        research=extract_text(result.content)
    )

    response = writer_agent_loop(research_output)
    print(response.markdowncd)


def writer_agent_loop(research_output: ResearchOutput):

    result = writer_agent.invoke(research_output)

    result = execute_tool_loop(
        writer_agent,
        tool_registry,
        result
    )

    return WriterOutput(
        markdown=extract_text(result.content)
    )


def extract_text(content):

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "\n".join(
            block["text"]
            for block in content
            if block.get("type") == "text"
        )

    return str(content)
