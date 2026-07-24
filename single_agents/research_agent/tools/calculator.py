import numexpr as ne
from langchain.tools import tool


@tool
def calculator(expression: str) -> float:
    '''Calculate a given expression'''
    result = ne.evaluate(expression)
    return float(result)
