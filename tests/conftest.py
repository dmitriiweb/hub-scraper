import shutil

import pytest

from hub_scraper.console.models import DataFolder, Hub


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
