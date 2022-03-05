from ._types import ScraperSettings


class HabrScraper:
    def __init__(self, settings: ScraperSettings):
        self.settings = settings
