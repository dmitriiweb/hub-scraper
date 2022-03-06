from datetime import datetime
from typing import Generator, Iterable

from hub_scraper.articles import ArticleListing

from .article_filter import ArticleFilter


class UpVotesCountFilter(ArticleFilter):
    def __init__(self, *args):
        self.threshold = int(args[0])
        super().__init__(*args)

    def filter_articles(
        self, articles: Iterable[ArticleListing]
    ) -> Generator[ArticleListing, None, None]:
        for article in articles:
            if article.statistics.votes_count >= self.threshold:
                yield article
