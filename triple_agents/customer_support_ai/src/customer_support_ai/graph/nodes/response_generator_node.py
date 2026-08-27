from customer_support_ai.agents.response_generator_agent import response_generator_agent
from customer_support_ai.graph.state import SupportState


def response_generator_node(state: SupportState) -> dict:
    query = state['user_query']
    intent = state['intent']
    articles = state['retrieved_documents']
    response = response_generator_agent.generate_response(
        query=query, intent=intent, articles=articles)

    return {
        'response': response
    }
