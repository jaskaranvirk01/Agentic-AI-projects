from stock_research.schemas.market import CompanyMarketData


def normalize_market_data(company_data: dict, global_quote_data: dict) -> CompanyMarketData:
    '''Normalizes the data from two different data dictionaries and combine them into a single pydantic object'''
    global_quote = global_quote_data['Global Quote']
    data = {**company_data, **global_quote}
    percentage = data['10. change percent'].split('%')
    return CompanyMarketData(
        ticker=data['Symbol'],
        company_name=data['Name'],
        sector=data['Sector'],
        industry=data['Industry'],
        description=data["Description"],
        market_cap=int(data['MarketCapitalization']),
        current_price=float(data['05. price']),
        price_change=float(data['09. change']),
        price_change_percent=float(percentage[0]),
        volume=int(data['06. volume'])
    )
