import asyncio

from typing import AsyncIterator, List, Optional

import httpx

from loguru import logger

from hub_scraper.articles import ArticleListing

from ._types import Article, ArticleFilter, DataFolder, Hub


class HabrScraper:
    request_headers = {"user-agent": "hub-scraper"}

    def __init__(
        self,
        hub: Hub,
        article_filters: List[ArticleFilter],
        data_folder: DataFolder,
    ):
        self.hub = hub
        self.article_filters = article_filters
        self.data_folder = data_folder

        self.semaphore = asyncio.Semaphore(self.hub.threads_number)
        self.client = httpx.AsyncClient()

    async def get_articles(self) -> AsyncIterator[Article]:
        article_listings = self._get_articles_listing()
        async for i in article_listings:
            filtered_articles = self._filter_articles(i)

        await self.client.aclose()

    async def _get_articles_listing(self) -> AsyncIterator[ArticleListing]:
        urls = self.hub.listing_pages_generator()
        for url in urls:
            response = await self._get(url)
            if response is None:
                continue
            for _, v in response.json()["articleRefs"].items():
                yield ArticleListing(**v)

    async def get_article(self, url: str) -> Article:
        pass

    async def _get(self, url: str) -> Optional[httpx.Response]:
        try:
            logger.info(f"Getting data from {url}")
            response = await self.client.get(url, headers=self.request_headers)
            return response
        except Exception as e:
            logger.error(f"Cannot get data from {url} {e}")

        return None

    def _filter_articles(self, article_listing: ArticleListing) -> List[ArticleListing]:
        for art_filter in self.article_filters:
            article_listing = art_filter.filter_articles(article_listing)
        return article_listing
