from pathlib import Path
from typing import List, Protocol


class ScraperSettings(Protocol):
    hub_url: str
    threads_number: int
    time_delay: int


class DataFolder(Protocol):
    articles_folder: Path


class ArticleListing(Protocol):
    url: str


class ArticlesFilter(Protocol):
    def filter_articles(self, articles: List[ArticleListing]) -> List[ArticleListing]:
        ...
