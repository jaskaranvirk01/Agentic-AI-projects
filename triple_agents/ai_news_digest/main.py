import logging

from agent.analysis_agent import analysis_agent
from agent.research_agent import research_agent
from agent.writer_agent import writer_agent
from loops.agent_loops import run_agent


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    query = input("Topic to explore news about: ")
    research_response = run_agent(
        research_agent,
        query,
    )

    analysis_response = run_agent(
        analysis_agent,
        research_response,
    )

    writer_response = run_agent(
        writer_agent,
        analysis_response,
    )

    logger.info(writer_response.content)


if __name__ == "__main__":
    main()
