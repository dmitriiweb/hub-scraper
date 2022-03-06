import hub_scraper.console.utils as cli_utils

from hub_scraper.articles.filters.min_datetime_filter import MinDateTimeFilter
from hub_scraper.articles.filters.post_type_filter import PostTypeFilter
from hub_scraper.articles.filters.up_votes_count_filter import UpVotesCountFilter


def test_get_min_datetime_filter():
    dt = "23-12-2020 12:12"
    f = cli_utils.get_min_datetime_filter(dt)
    assert isinstance(f, MinDateTimeFilter)


def test_get_filter_post_type():
    article_types = "article, news"
    f = cli_utils.get_filter_post_type(article_types)
    assert isinstance(f, PostTypeFilter)


def test_get_filter_up_votes_count():
    up_votes_count = 10
    f = cli_utils.get_up_votes_count_filter(up_votes_count)
    assert isinstance(f, UpVotesCountFilter)
