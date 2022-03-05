from datetime import datetime
from typing import Generator, Iterable

from hub_scraper.articles import ArticleListing

from .article_filter import ArticleFilter


class MinDateTimeFilter(ArticleFilter):
    def __init__(self, *args):
        try:
            self.threshold: datetime = args[0]
        except IndexError:
            raise ValueError("MinDateTimeFilter requires a threshold datetime")

        if not isinstance(self.threshold, datetime):
            raise ValueError(
                "MinDateTimeFilter requires a datetime object as threshold"
            )

        super().__init__(*args)

    def filter_articles(
        self, articles: Iterable[ArticleListing]
    ) -> Generator[ArticleListing, None, None]:
        for article in articles:
            if article.time_published >= self.threshold:
                yield article
