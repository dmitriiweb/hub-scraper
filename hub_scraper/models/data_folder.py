from pathlib import Path


class DataFolder:
    articles_folder_name = "articles"
    index_folder_name = "index"

    def __init__(self, data_folder: str):
        self.data_folder = Path(data_folder)
        self._create_folders()

    @property
    def articles_folder(self) -> Path:
        return self.data_folder / self.articles_folder_name

    @property
    def index_folder(self) -> Path:
        return self.data_folder / self.index_folder_name

    def _create_folders(self):
        self.articles_folder.mkdir(parents=True, exist_ok=True)
