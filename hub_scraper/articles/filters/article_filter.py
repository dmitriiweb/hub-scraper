from abc import ABC, abstractmethod
from typing import List, Protocol

from hub_scraper.articles import ArticleListing


class Article(Protocol):
    ...


class ArticleFilter(ABC):
    def __init__(self, *args):
        pass

    @abstractmethod
    def filter_articles(self, articles: List[Article]) -> List[ArticleListing]:
        ...
