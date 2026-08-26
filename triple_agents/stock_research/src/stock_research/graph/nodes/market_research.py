from stock_research.agents.market_research_agent import market_research_agent
from stock_research.graph.state import StockResearchState


def market_research_node(state: StockResearchState) -> dict:
    research_data = market_research_agent.run(state['ticker'])

    return {
        'research': research_data
    }
