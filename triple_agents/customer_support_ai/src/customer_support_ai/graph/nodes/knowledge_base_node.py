from customer_support_ai.agents.knowledge_base_agent import knowledge_base_agent
from customer_support_ai.graph.state import SupportState


def knowledge_base_node(state: SupportState) -> dict:
    query = state['user_query']
    intent = state['intent']
    response = knowledge_base_agent.get_documents(
        query=query, intent=intent, limit=3)

    return {
        'retrieved_documents': response
    }
