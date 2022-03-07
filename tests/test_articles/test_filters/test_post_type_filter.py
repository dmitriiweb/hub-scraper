from dataclasses import dataclass

import pytest

from hub_scraper.articles.filters import ArticleFilterType, get_filter


@dataclass
class Article:
    post_type: str


def get_article(atype: str) -> Article:
    return Article(atype)


@pytest.mark.parametrize(
    "atype, result",
    (
        [get_article("article"), False],
        [get_article("news"), False],
        [get_article("ad"), True],
    ),
)
def test_post_type_filter(atype, result):
    threshold = ["article", "news"]
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.post_type_filter
    )
    filtered_article = article_filter.filter_article(atype)  # type: ignore
    res = filtered_article is None
    assert res == result
