from langchain.tools import tool
import numexpr as ne


@tool
def calculator(expression: str) -> float:
    '''Calculate the given expression'''
    res = ne.evaluate(expression)
    return float(res)
