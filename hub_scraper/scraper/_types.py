from pathlib import Path
from typing import List, Protocol

from hub_scraper.articles import ArticleListing


class Hub(Protocol):
    def get_page_url(self, page_number: int) -> str:
        ...


class DataFolder(Protocol):
    articles_folder: Path


class ArticleFilter(Protocol):
    def filter_articles(self, articles: List[ArticleListing]) -> List[ArticleListing]:
        ...


class Article(Protocol):
    url: str
