from langchain.tools import tool
import numexpr as ne


@tool
def calculator(expression: str) -> float:
    """Evaluate a mathematical expression and return the result as a float."""
    try:
        result = ne.evaluate(expression)
        return float(result)
    except Exception:
        return "Invalid mathematical expression."
