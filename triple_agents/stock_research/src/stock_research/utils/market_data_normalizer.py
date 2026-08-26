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
        volume=int(data['06. volume']),
        pe_ratio=float(data['PERatio']),
        forward_pe=float(data['ForwardPE']),
        peg_ratio=float(data['PEGRatio']),
        price_to_sales=float(data['PriceToSalesRatioTTM']),
        price_to_book=float(data['PriceToBookRatio']),
        ev_to_revenue=float(data['EVToRevenue']),
        ev_to_ebitda=float(data['EVToEBITDA']),
        eps=float(data['EPS']),
        profit_margin=float(data['ProfitMargin']),
        operating_margin=float(data['OperatingMarginTTM']),
        return_on_assets=float(data['ReturnOnAssetsTTM']),
        return_on_equity=float(data['ReturnOnEquityTTM']),
        revenue_ttm=int(data['RevenueTTM']),
        quarterly_revenue_growth=float(data['QuarterlyRevenueGrowthYOY']),
        quarterly_earnings_growth=float(data['QuarterlyEarningsGrowthYOY']),
        dividend_per_share=float(data['DividendPerShare']),
        dividend_yield=float(data['DividendYield']),
        beta=float(data['Beta']),
        fifty_two_week_high=float(data['52WeekHigh']),
        fifty_two_week_low=float(data['52WeekLow']),
    )
