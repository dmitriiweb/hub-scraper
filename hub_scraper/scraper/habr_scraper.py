from typing import List

from hub_scraper.articles import ArticleListing

from ._types import Article, ArticleFilter, DataFolder, Hub


class HabrScraper:
    def __init__(
        self,
        hub: Hub,
        article_filters: List[ArticleFilter],
        data_folder: DataFolder,
    ):
        self.hub = hub
        self.article_filters = article_filters
        self.data_folder = data_folder

    def get_articles_listing(self) -> List[ArticleListing]:
        urls = self.hub.listing_pages_generator()
        print(urls)

    def get_article(self, url: str) -> Article:
        pass
