from enum import Enum, auto

from .article_filter import ArticleFilter
from .min_datetime_filter import MinDateTimeFilter


class ArticleFilterType(Enum):
    """
    Enum of all possible article filters
    """

    min_datetime_filter = auto()


FILTERS = {ArticleFilterType.min_datetime_filter: MinDateTimeFilter}


def get_filter(*args, filter_type: ArticleFilterType) -> ArticleFilter:
    """
    Returns a filter function for a given filter type
    """
    try:
        return FILTERS[filter_type](*args)
    except KeyError:
        raise ValueError(f"No filter for type {filter_type}")
