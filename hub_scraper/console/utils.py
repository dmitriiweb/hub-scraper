from datetime import datetime
from typing import List, Optional

from hub_scraper.articles.filters import ArticleFilter, ArticleFilterType, get_filter


def get_article_filters(
    *,
    filter_min_datetime: Optional[str],
    filter_post_type: Optional[str],
    filter_up_votes_count: int,
) -> List[ArticleFilter]:
    filters = []

    if filter_min_datetime:
        filters.append(get_min_datetime_filter(filter_min_datetime))

    if filter_post_type:
        filters.append(get_filter_post_type(filter_post_type))

    filters.append(get_up_votes_count_filter(filter_up_votes_count))

    return filters


def get_min_datetime_filter(datetime_val: str) -> ArticleFilter:
    """
    Returns a filter for the minimum datetime.

    Args:
        datetime_val: must be in format dd-mm-yyyy hh:mm

    """
    dt = datetime.strptime(datetime_val, "%d-%m-%Y %H:%M")
    try:
        return get_filter(dt, filter_type=ArticleFilterType.min_datetime_filter)
    except ValueError:
        raise ValueError(
            f"Invalid datetime value: {datetime_val}. Must be in format dd-mm-yyyy hh:mm"
        )


def get_filter_post_type(post_types: str):
    """
    Returns a filter for the post types.

    Args:
        post_types: must be a list of post types separated by comma, e.g. "article, news"
    """
    post_types = [i.strip() for i in post_types.split(",")]
    f = get_filter(post_types, filter_type=ArticleFilterType.post_type_filter)
    return f


def get_up_votes_count_filter(up_votes_count: int):
    """
    Returns a filter for the minimum up votes count.

    Args:
        up_votes_count: must be an integer
    """
    f = get_filter(up_votes_count, filter_type=ArticleFilterType.up_votes_filter)
    return f