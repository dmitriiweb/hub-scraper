from dataclasses import dataclass
from datetime import datetime
from typing import List

from hub_scraper.articles.filters import ArticleFilterType, get_filter


@dataclass
class Article:
    time_published: datetime


def get_articles() -> List[Article]:
    times = [
        "2020-06-01 23:59",
        "2020-07-01 23:59",
        "2020-02-01 23:59",
    ]
    articles = [Article(datetime.strptime(time, "%Y-%m-%d %H:%M")) for time in times]
    return articles


def test_min_datetime_filter():
    threshold = "2020-04-01 23:59"
    threshold = datetime.strptime(threshold, "%Y-%m-%d %H:%M")
    article_filter = get_filter(
        threshold, filter_type=ArticleFilterType.min_datetime_filter
    )
    filtered_articles = article_filter.filter_articles(get_articles())  # type: ignore
    assert len(list(filtered_articles)) == 2
