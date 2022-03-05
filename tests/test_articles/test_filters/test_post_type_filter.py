from dataclasses import dataclass
from typing import List

from hub_scraper.articles.filters import ArticleFilterType, get_filter


@dataclass
class Article:
    post_type: str


def get_articles() -> List[Article]:
    article_types = ["article", "news", "ad"]
    articles = [Article(i) for i in article_types]
    return articles


def test_post_type_filter():
    threshold = ["article", "news"]
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.post_type_filter
    )
    filtered_articles = article_filter.filter_articles(get_articles())
    assert len(list(filtered_articles)) == 2
