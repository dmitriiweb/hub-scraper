import asyncio

from typing import AsyncIterator, List, Optional

import httpx

from loguru import logger

from hub_scraper.articles import Article, ArticleListing

from ._types import ArticleFilter, DataFolder, Hub


class HabrScraper:
    request_headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/99.0.4844.45 Safari/537.36"
    }

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
            filtered_i = self._filter_article(i)
            if filtered_i is None:
                continue

            try:
                article = await self.get_article(filtered_i.article_url)
                yield article
            except Exception as e:
                logger.error(f"Cannot get article from {filtered_i.article_url} {e}")

        await self.client.aclose()

    async def _get_articles_listing(self) -> AsyncIterator[ArticleListing]:
        urls = self.hub.listing_pages_generator()
        for url in urls:
            response = await self._get(url)
            if response is None:
                continue
            for _, v in response.json()["articleRefs"].items():
                yield ArticleListing(**v)

    async def get_article(self, url: str) -> Optional[Article]:
        response = await self._get(url)
        article = Article.from_response(response)
        return article

    async def _get(self, url: str) -> Optional[httpx.Response]:
        try:
            logger.info(f"Getting data from {url}")
            response = await self.client.get(
                url, headers=self.request_headers, follow_redirects=True
            )
            return response
        except Exception as e:
            logger.error(f"Cannot get data from {url} {e}")

        return None

    def _filter_article(
        self, article_listing: ArticleListing
    ) -> Optional[ArticleListing]:
        for art_filter in self.article_filters:
            article_listing = art_filter.filter_article(article_listing)

            if article_listing is None:
                return None

        return article_listing
