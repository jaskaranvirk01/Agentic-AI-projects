from langchain.tools import tool
import pandas as pd


@tool
def read_csv(_: str = ""):
    """Reads expense CSV file and returns expense data."""
    data = pd.read_csv("data/expenses.csv")
    return data.to_json()
