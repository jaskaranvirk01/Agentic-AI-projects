import string
import json


class KnowledgeService:
    def __init__(self, file_path: str):
        self.articles = self._load_articles(file_path=file_path)

    def _load_articles(self, file_path: str) -> list:
        with open(file_path, 'r') as f:
            articles = json.load(f)

        return articles

    def search(self, query: str, intent: str, limit=3) -> list:
        filtered_articles = []
        for article in self.articles:
            if article['category'] == intent:
                filtered_articles.append(article)

        scored_articles = self._score_candidates(
            query=query, articles=filtered_articles)

        sorted_articles = sorted(
            scored_articles, key=lambda article: article['score'], reverse=True)

        selected_articles = [article['article']
                             for article in sorted_articles if article['score'] > 0]

        return selected_articles[:limit]

    def _score_candidates(self, query: str, articles: list):
        query_words = query.split(' ')
        score_list = []
        for article in articles:
            article_text = article['title'] + \
                str(' '.join(article['keywords'])) + article['problem']
            article_words = article_text.split(' ')
            score = 0
            for article_word in article_words:
                for query_word in query_words:
                    if self._normalize_word(article_word) == self._normalize_word(query_word):
                        score += 1
            scores = {
                'article': article,
                'score': score
            }
            score_list.append(scores)

        return score_list

    def _normalize_word(self, word: str):
        punctuation = string.punctuation
        cleaned_word = [c for c in word if c not in punctuation]
        return (''.join(cleaned_word)).lower()

    def get_intents(self):
        intents = [article['category'] for article in self.articles]
        return set(intents)


knowledge_service = KnowledgeService(
    'src/customer_support_ai/data/knowledge_base.json')
