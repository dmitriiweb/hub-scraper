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

    def get_articles_listing(self, url: str) -> List[ArticleListing]:
        pass

    def get_article(self, url: str) -> Article:
        pass

    def listing_pages_generator(self) -> List[str]:
        urls = []
        for page_number in range(1, self.hub.max_page + 1):
            url = self.hub.get_page_url(page_number)
            if url:
                urls.append(url)
        return urls
