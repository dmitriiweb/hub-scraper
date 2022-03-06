from pathlib import Path
from typing import List, Protocol

from hub_scraper.articles import ArticleListing


class ScraperSettings(Protocol):
    hub_name: str
    threads_number: int
    time_delay: int
    max_page: int


class DataFolder(Protocol):
    articles_folder: Path


class ArticlesFilter(Protocol):
    def filter_articles(self, articles: List[ArticleListing]) -> List[ArticleListing]:
        ...


class Article(Protocol):
    url: str
