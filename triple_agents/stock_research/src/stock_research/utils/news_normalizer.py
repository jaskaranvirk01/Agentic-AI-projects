from stock_research.schemas.company_news import NewsArticle, CompanyNews
from datetime import datetime


def normalize_company_news(ticker: str, data: dict) -> CompanyNews:
    '''Use this function to normalize the raw news data and convert it into a proper pydantic response object'''
    articles = []

    for article in data['feed']:
        for t in article['ticker_sentiment']:
            if t['ticker'] != ticker:
                continue
            relevance_score = float(t['relevance_score'])
            if relevance_score < 0.6:
                continue
            articles.append(
                NewsArticle(
                    title=article['title'],
                    summary=article['summary'],
                    source=article['source'],
                    url=article['url'],
                    time_published=datetime.strptime(
                        article['time_published'], '%Y%m%dT%H%M%S')
                )
            )
            break
        if len(articles) >= 10:
            break
    return CompanyNews(
        ticker=ticker,
        articles=articles
    )
