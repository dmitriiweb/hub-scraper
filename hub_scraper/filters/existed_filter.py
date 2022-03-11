from datetime import datetime
from typing import Optional

from hub_scraper.models import ArticleListing

from .article_filter import ArticleFilter


class ExistedFilter(ArticleFilter):
    def __init__(self, *args):
        super().__init__(*args)

    def filter_article(self, article: ArticleListing) -> Optional[ArticleListing]:
        pass
