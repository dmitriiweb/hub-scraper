from dataclasses import dataclass
from datetime import datetime

import pytest

from hub_scraper.filters import ArticleFilterType, get_filter


@dataclass
class Article:
    time_published: datetime


def get_article(dt: str) -> Article:
    return Article(datetime.strptime(dt, "%Y-%m-%d %H:%M"))


@pytest.mark.parametrize(
    "article, result",
    (
        [get_article("2020-06-01 23:59"), False],
        [get_article("2020-07-01 23:59"), False],
        [get_article("2020-02-01 23:59"), True],
    ),
)
def test_min_datetime_filter(article, result):
    threshold = "2020-04-01 23:59"
    threshold = datetime.strptime(threshold, "%Y-%m-%d %H:%M")
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.min_datetime_filter
    )
    filtered_article = article_filter.filter_article(article)  # type: ignore
    res = filtered_article is None
    assert res == result


def test_min_datetime_filter_error_wrong_type():
    with pytest.raises(ValueError) as error:
        get_filter("str", filter_type=ArticleFilterType.min_datetime_filter)

    assert "requires a datetime object" in str(error.value)
