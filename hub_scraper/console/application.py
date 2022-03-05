import asyncio

from functools import wraps
from pathlib import Path
from typing import Optional

import click


def coro(f):
    """
    Make click async:
    https://github.com/pallets/click/issues/85
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@coro
@click.option(
    "-u",
    "--url",
    help="Hab to scrape, e.g. https://habr.com/ru/hub/python/",
    type=str,
    required=True,
)
@click.option(
    "-of",
    "--output-folder",
    help="Folder to save scraped data, e.g. /home/user/data",
    type=str,
    required=True,
)
@click.option(
    "-t",
    "--threads",
    help="Number async requests to the website, default: 1",
    type=int,
    required=False,
    default=1,
)
@click.option(
    "-d",
    "--time-delay",
    help="Time delay between requests to the website, default: 1",
    type=int,
    required=False,
    default=1,
)
@click.option(
    "--images",
    help="If true will download images from articles locally, if not in downloaded articles will be urls to images. Default False",
    type=bool,
    required=False,
    default=False,
    is_flag=True,
)
@click.option(
    "--no-sandbox",
    help="If true will skip articles from the sandbox. Default False",
    type=bool,
    required=False,
    default=False,
    is_flag=True,
)
@click.option(
    "-fr",
    "--filter-rating",
    help="Filter articles by rating, default: 0",
    type=int,
    required=False,
    default=0,
)
@click.option(
    "-fc",
    "--filter-comments",
    help="Filter articles by comments count, default: 0",
    type=int,
    required=False,
    default=0,
)
@click.option(
    "-fc",
    "--filter-comments",
    help="Filter articles by comments count, default: 0",
    type=int,
    required=False,
    default=0,
)
@click.option(
    "-fb",
    "--filter-bookmarks",
    help="Filter articles by bookmarks count, default: 0",
    type=int,
    required=False,
    default=0,
)
@click.option(
    "-fb",
    "--filter-tags",
    help='Filter articles by list of tags, e.g. "Django, tutorial". Default: None',
    type=str,
    required=False,
    default=None,
)
@click.option(
    "-fk",
    "--filter-keywords",
    help='Filter articles by list of key-words for title, e.g. "Django, tutorial". Default: None',
    type=str,
    required=False,
    default=None,
)
@click.option(
    "-fd",
    "--filter-date",
    help='Filter articles by date, e.g. "dd-mm-yyyy hh:mm". Default: None',
    type=str,
    required=False,
    default=None,
)
@click.option(
    "-fa",
    "--filter-author",
    help='Filter articles by list of authors, e.g. "he_boiko, OldTech". Default: None',
    type=str,
    required=False,
    default=None,
)
async def main(
    url: str,
    output_folder: str,
    threads: int,
    time_delay: int,
    images: bool,
    no_sandbox: bool,
    filter_comments: int,
    filter_rating: int,
    filter_bookmarks: int,
    filter_tags: Optional[str],
    filter_keywords: Optional[str],
    filter_date: Optional[str],
    filter_author: Optional[str],
):
    output_folder = Path(output_folder)


if __name__ == "__main__":
    main()
