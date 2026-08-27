from stock_research.graph.state import StockResearchState
from stock_research.agents.final_report_writer_agent import final_report_writer_agent


def final_report_writer_node(state: StockResearchState) -> dict:
    research_data = state['research']
    financial_analysis = state['financial_analysis']

    report = final_report_writer_agent.run(
        research_data=research_data, financial_analysis=financial_analysis)

    return {'final_report': report}
