from customer_support_ai.graph.nodes.intent_detection_node import intent_detection_node
from customer_support_ai.graph.nodes.knowledge_base_node import knowledge_base_node
from customer_support_ai.graph.nodes.response_generator_node import response_generator_node
from langgraph.graph import StateGraph, START, END
from customer_support_ai.graph.state import SupportState


def route_query(state: SupportState) -> str:
    if state['intent'].lower() == 'general':
        return 'response_generation'
    else:
        return 'knowledge_base'


builder = StateGraph(SupportState)


builder.add_node('intent_detection', intent_detection_node)
builder.add_node('knowledge_base', knowledge_base_node)
builder.add_node('response_generation', response_generator_node)

builder.add_edge(START, 'intent_detection')
builder.add_conditional_edges('intent_detection', route_query)
builder.add_edge('knowledge_base', 'response_generation')
builder.add_edge('response_generation', END)

graph = builder.compile()


result = graph.invoke({
    'user_query': 'hello',
    'intent':  None,
    'intent_confidence':  None,
    'retrieved_documents':  None,
    'response':  None
}
)

print(result)
