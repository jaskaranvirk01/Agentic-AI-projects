from customer_support_ai.agents.intent_detection_agent import intent_detection_agent
from customer_support_ai.graph.state import SupportState


def intent_detection_node(state: SupportState) -> dict:
    query = state['user_query']
    response = intent_detection_agent.detect_intent(query=query)

    return {
        'intent': response.intent,
        'intent_confidence': response.intent_confidence
    }
