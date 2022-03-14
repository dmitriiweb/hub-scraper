import shutil

from pathlib import Path
from typing import Generator

import pytest

from hub_scraper.models import DataFolder, Hub
from hub_scraper.scraper import HabrScraper


BASEDIR = Path(__file__).resolve().parent


@pytest.fixture()
def default_hub() -> Hub:
    return Hub(
        hub_name="python",
        threads_number=1,
        time_delay=2,
        max_page=50,
        min_up_votes=None,
    )


@pytest.fixture()
def default_data_folder() -> DataFolder:
    yield DataFolder(data_folder="test_outputs")
    shutil.rmtree("test_outputs")


@pytest.fixture()
def default_scraper(default_hub, default_data_folder) -> HabrScraper:
    return HabrScraper(default_hub, [], default_data_folder)


@pytest.fixture()
def data_folder_path() -> Generator[Path, None, None]:
    test_folder = BASEDIR.joinpath("test_data")
    test_folder.mkdir(exist_ok=True, parents=True)
    article_folder = test_folder.joinpath("111")
    article_folder.mkdir(exist_ok=True, parents=True)
    yield test_folder
    shutil.rmtree(test_folder)
