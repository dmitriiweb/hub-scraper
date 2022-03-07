import asyncio

from typing import AsyncIterator, List

import httpx

from loguru import logger

from hub_scraper.articles import ArticleListing

from ._types import Article, ArticleFilter, DataFolder, Hub


async def _get(
    urls: List[str], semaphore: asyncio.Semaphore, time_sleep: float
) -> AsyncIterator[httpx.Response]:
    async with semaphore:
        async with httpx.AsyncClient() as client:
            for url in urls:
                try:
                    logger.info(f"Getting data from {url}")
                    response = await client.get(
                        url, headers={"User-Agent": "hub-scraper"}
                    )
                    yield response
                    await asyncio.sleep(time_sleep)
                except Exception as e:
                    logger.error(f"Cannot get data from {url} {e}")


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

        self.httpx_client = httpx.AsyncClient()

    async def get_articles(self) -> AsyncIterator[Article]:
        article_listings = self._get_articles_listing()
        async for i in article_listings:
            print(i)

    async def _get_articles_listing(self) -> AsyncIterator[ArticleListing]:
        urls = self.hub.listing_pages_generator()
        semaphore = asyncio.Semaphore(self.hub.threads_number)
        responses = _get(urls, semaphore, self.hub.time_delay)
        async for response in responses:
            data = response.json()
            for _, v in data["articleRefs"].items():
                yield ArticleListing(**v)

    async def get_article(self, url: str) -> Article:
        pass
