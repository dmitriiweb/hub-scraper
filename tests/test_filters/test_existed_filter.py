from dataclasses import dataclass
from pathlib import Path

import pytest

from hub_scraper.filters import ArticleFilterType, get_filter


@dataclass
class Article:
    id: str


def get_article(article_id: str) -> Article:
    return Article(article_id)


@pytest.mark.parametrize(
    "article, result",
    (
        [get_article("111"), True],
        [get_article("333"), False],
        [get_article("222"), False],
    ),
)
def test_existed_filter(data_folder_path: Path, article: Article, result: bool):
    article_filter = get_filter(
        data_folder_path, filter_type=ArticleFilterType.existed_filter
    )
    filtered_article = article_filter.filter_article(article)  # type: ignore
    res = filtered_article is None
    assert res == result
