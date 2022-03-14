from typing import Optional, Protocol

import pytest


EXPECTED_URLS = [
    "https://habr.com/kek/v2/articles/?hub=python&sort=all&fl=ru&hl=ru&page=1",
    None,
]


class Hub(Protocol):
    def get_page_url(self, page_number: int) -> Optional[str]:
        ...


@pytest.mark.parametrize(
    "page_number, expected_url", ([1, EXPECTED_URLS[0]], [100, EXPECTED_URLS[1]])
)
def test_get_page_url(page_number: int, expected_url: str, default_hub: Hub):
    assert default_hub.get_page_url(page_number) == expected_url
