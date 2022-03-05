from pathlib import Path
from typing import List, Protocol


class ScraperSettings(Protocol):
    hub_name: str
    threads_number: int
    time_delay: int
    max_page: int


class DataFolder(Protocol):
    articles_folder: Path


class ArticleListing(Protocol):
    url: str


class Article(Protocol):
    url: str
    title: str
    content: str


class ArticlesFilter(Protocol):
    def filter_articles(self, articles: List[ArticleListing]) -> List[ArticleListing]:
        ...
