from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlencode


@dataclass()
class Hub:
    hub_name: str
    threads_number: int
    time_delay: int
    max_page: int
    min_up_votes: Optional[int]
    _max_pages: int = 50
    _base_api_url: str = "https://habr.com/kek/v2/articles/?{params}"

    def get_page_url(self, page_number: int) -> Optional[str]:
        if page_number > self._max_pages:
            return None

        url_params = self._get_url_params(page_number)
        url = self._base_api_url.format(params=url_params)
        return url

    def _get_url_params(self, page_number: int) -> str:
        # hub=python&sort=all&fl=ru&hl=ru&page=1
        url_params = {
            "hub": self.hub_name,
            "sort": "all",
            "fl": "ru",
            "hl": "ru",
            "page": page_number,
        }
        if self.min_up_votes:
            url_params["score"] = self.min_up_votes

        return urlencode(url_params)


class DataFolder:
    articles_folder_name = "articles"

    def __init__(self, data_folder: str):
        self.data_folder = Path(data_folder)
        self._create_folders()

    @property
    def articles_folder(self) -> Path:
        return self.data_folder / self.articles_folder_name

    def _create_folders(self):
        self.articles_folder.mkdir(parents=True, exist_ok=True)
