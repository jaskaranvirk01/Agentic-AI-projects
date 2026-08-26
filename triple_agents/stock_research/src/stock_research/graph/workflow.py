from langgraph.graph import StateGraph, START, END
from stock_research.graph.nodes.market_research import market_research_node
from stock_research.graph.state import StockResearchState
from stock_research.graph.nodes.financial_analysis_node import financial_analysis_node

builder = StateGraph(StockResearchState)


builder.add_node('market_research', market_research_node)
builder.add_node('financial_analysis', financial_analysis_node)


builder.add_edge(START, 'market_research')
builder.add_edge('market_research', 'financial_analysis')
builder.add_edge('financial_analysis', END)


graph = builder.compile()


result = graph.invoke({
    "ticker": "IBM",
    "research": None,
    "financial_analysis": None,
    "final_report": None,
})


print(result)
