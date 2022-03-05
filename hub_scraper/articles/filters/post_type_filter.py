from typing import Generator, List

from hub_scraper.articles import ArticleListing

from .article_filter import ArticleFilter


class PostTypeFilter(ArticleFilter):
    def __init__(self, *args):
        self.article_types = set(*args)
        super().__init__(*args)

    def filter_articles(
        self, articles: List[ArticleListing]
    ) -> Generator[ArticleListing, None, None]:
        for article in articles:
            if article.post_type in self.article_types:
                yield article
