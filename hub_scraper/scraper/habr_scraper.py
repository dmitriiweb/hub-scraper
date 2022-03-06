from typing import List

from hub_scraper.articles import ArticleListing

from ._types import Article, ArticleFilter, DataFolder, Hub


class HabrScraper:
    def __init__(
        self,
        settings: Hub,
        article_filters: List[ArticleFilter],
        data_folder: DataFolder,
    ):
        self.settings = settings
        self.article_filters = article_filters
        self.data_folder = data_folder

    def get_articles_listing(self, url: str) -> List[ArticleListing]:
        pass

    def get_article(self, url: str) -> Article:
        pass

    def _listing_page_generator(self) -> List[str]:
        pass
