from enum import Enum, auto

from .article_filter import ArticleFilter
from .min_datetime_filter import MinDateTimeFilter
from .post_type_filter import PostTypeFilter
from .up_votes_count_filter import UpVotesCountFilter


class ArticleFilterType(Enum):
    """
    Enum of all possible article filters
    """

    min_datetime_filter = auto()
    post_type_filter = auto()
    up_votes_filter = auto()


FILTERS = {
    ArticleFilterType.min_datetime_filter: MinDateTimeFilter,
    ArticleFilterType.post_type_filter: PostTypeFilter,
    ArticleFilterType.up_votes_filter: UpVotesCountFilter,
}


def get_filter(*args, filter_type: ArticleFilterType) -> ArticleFilter:
    """
    Returns a filter function for a given filter type
    """
    try:
        return FILTERS[filter_type](*args)  # type: ignore
    except KeyError:
        raise ValueError(f"No filter for type {filter_type}")
