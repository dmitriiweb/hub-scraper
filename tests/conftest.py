import pytest

from hub_scraper.console.models import Hub


@pytest.fixture()
def default_hub() -> Hub:
    return Hub(
        hub_name="python",
        threads_number=1,
        time_delay=2,
        max_page=50,
        min_up_votes=None,
    )
