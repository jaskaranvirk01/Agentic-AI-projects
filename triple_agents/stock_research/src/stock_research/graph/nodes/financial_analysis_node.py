from stock_research.agents.financial_analysis_agent import financial_analysis_agent
from stock_research.graph.state import StockResearchState


def financial_analysis_node(state: StockResearchState) -> dict:
    data = state['research'].research_data.company_market_data

    analysis = financial_analysis_agent.run(data)
    return {
        'financial_analysis': analysis
    }
