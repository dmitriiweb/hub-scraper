from dataclasses import dataclass
from typing import List

from hub_scraper.articles.filters import ArticleFilterType, get_filter


@dataclass
class Statistics:
    votes_count: int


@dataclass
class Article:
    statistics: Statistics


def get_articles() -> List[Article]:
    votes = [i for i in range(10)]
    articles = [Article(Statistics(i)) for i in votes]
    return articles


def test_post_type_filter():
    threshold = 4
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.up_votes_filter
    )
    filtered_articles = article_filter.filter_articles(get_articles())  # type: ignore
    assert len(list(filtered_articles)) == 6


def test_empty_articles_list():
    threshold = 4
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.up_votes_filter
    )
    filtered_articles = article_filter.filter_articles([])
    assert len(list(filtered_articles)) == 0
