import asyncio
from pathlib import Path
from functools import wraps

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
async def main(url: str, output_folder: str, threads: int, time_delay: int, images: bool):
    output_folder = Path(output_folder)


if __name__ == "__main__":
    main()
