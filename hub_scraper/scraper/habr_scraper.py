from typing import Iterable, List

from hub_scraper.articles import ArticleListing

from ._types import Article, ArticlesFilter, DataFolder, ScraperSettings


class HabrScraper:
    def __init__(
        self,
        settings: ScraperSettings,
        article_filters: Iterable[ArticlesFilter],
        data_folder: DataFolder,
    ):
        self.settings = settings
        self.article_filters = article_filters
        self.data_folder = data_folder

    def get_articles_listing(self, url: str) -> List[ArticleListing]:
        pass

    def get_article(self, url: str) -> Article:
        pass

    def _get_total_pages(self) -> int:
        pass

    def _listing_page_generator(self) -> List[str]:
        pass
