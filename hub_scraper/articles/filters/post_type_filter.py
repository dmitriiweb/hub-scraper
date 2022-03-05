# from datetime import datetime
# from typing import Generator, List, Protocol
#
# from hub_scraper.articles import ArticleListing
#
# from .article_filter import ArticleFilter
#
#
# class Article(Protocol):
#     time_published: datetime
#
#
# class MinDateTimeFilter(ArticleFilter):
#     def __init__(self, *args):
#         try:
#             self.threshold: datetime = args[0]
#         except IndexError:
#             raise ValueError("MinDateTimeFilter requires a threshold datetime")
#
#         if not isinstance(self.threshold, datetime):
#             raise ValueError(
#                 "MinDateTimeFilter requires a datetime object as threshold"
#             )
#
#         super().__init__(*args)
#
#     def filter_articles(
#             self, articles: List[Article]
#     ) -> Generator[ArticleListing, None, None]:
