from agents.resume_reader_agent import resume_reader_agent
from agents.resume_improver_agent import resume_improve_agent
from tools.rewrite_resume import rewrite_resume
from tools.ats_scorer import ats_scorer
from tools.info_extractor import extract_resume_information
from tools.resume_reader import read_pdf
from rich import print
tools = {
    'rewrite_resume': rewrite_resume,
    'ats_scorer': ats_scorer,
    'extract_resume_information': extract_resume_information,
    'read_pdf': read_pdf
}


def execute_tool_loop(agent, tool_registry, result):

    tool_outputs = {}

    while result.tool_calls:

        for tool_call in result.tool_calls:

            tool_name = tool_call["name"]

            tool_result = tool_registry[tool_name].invoke(
                tool_call["args"]
            )

            tool_outputs[tool_name] = tool_result

            agent.add_tool_message(
                tool_result=tool_result,
                tool_call=tool_call
            )

        result = agent.continue_conversation()

    return result, tool_outputs


def resume_reader_loop(user_query: str):
    resume_reader_agent.reset()
    result = resume_reader_agent.invoke(user_query)

    _, outputs = execute_tool_loop(
        resume_reader_agent,
        tools,
        result
    )
    if "extract_resume_information" not in outputs:
        print(result.content)
        return
    resume_analysis = outputs.get("extract_resume_information")

    if resume_analysis is None:
        raise RuntimeError("Resume analysis was not generated.")

    final_response = improve_agent_loop(resume_analysis)

    print(final_response)


def improve_agent_loop(resume_analysis):
    resume_improve_agent.reset()
    result = resume_improve_agent.invoke(resume_analysis)

    _, outputs = execute_tool_loop(
        resume_improve_agent,
        tools,
        result
    )

    rewritten_resume = outputs.get("rewrite_resume")

    if rewritten_resume is None:
        raise RuntimeError("Resume was not rewritten.")

    return rewritten_resume
