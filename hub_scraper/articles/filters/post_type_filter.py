from typing import Generator, List, Protocol

from hub_scraper.articles import ArticleListing

from .article_filter import ArticleFilter


class Article(Protocol):
    post_type: str


class PostTypeFilter(ArticleFilter):
    def __init__(self, *args):
        self.article_types = set(*args)
        super().__init__(*args)

    def filter_articles(
        self, articles: List[Article]
    ) -> Generator[ArticleListing, None, None]:
        for article in articles:
            if article.post_type in self.article_types:
                yield article
