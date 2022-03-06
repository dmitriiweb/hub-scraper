from pathlib import Path
from typing import List, Protocol

from hub_scraper.articles import ArticleListing


class Hub(Protocol):
    def listing_pages_generator(self) -> List[str]:
        ...


class DataFolder(Protocol):
    articles_folder: Path


class ArticleFilter(Protocol):
    def filter_articles(self, articles: List[ArticleListing]) -> List[ArticleListing]:
        ...


class Article(Protocol):
    url: str
