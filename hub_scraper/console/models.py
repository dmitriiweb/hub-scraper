from dataclasses import dataclass
from pathlib import Path


@dataclass()
class ScraperSettings:
    hub_name: str
    threads_number: int
    time_delay: int
    max_page: int


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
