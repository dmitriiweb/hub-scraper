import hub_scraper.console.utils as cli_utils

from hub_scraper.filters.min_datetime_filter import MinDateTimeFilter
from hub_scraper.filters.post_type_filter import PostTypeFilter


def test_get_min_datetime_filter():
    dt = "23-12-2020 12:12"
    f = cli_utils.get_min_datetime_filter(dt)
    assert isinstance(f, MinDateTimeFilter)


def test_get_filter_post_type():
    article_types = "article, news"
    f = cli_utils.get_filter_post_type(article_types)
    assert isinstance(f, PostTypeFilter)
