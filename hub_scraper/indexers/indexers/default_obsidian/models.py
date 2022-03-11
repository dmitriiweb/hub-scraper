import asyncio
import json

from pathlib import Path
from typing import List, Tuple

from aiofile import async_open
from loguru import logger

from hub_scraper import conf
from hub_scraper.models import ArticleMeta


class Metas(Tuple[ArticleMeta, ...]):
    @classmethod
    async def from_folders(cls, article_folders: List[Path]) -> "Metas":
        tasks = [cls._get_meta_from_folder(i) for i in article_folders]
        metas = await asyncio.gather(*tasks)
        return cls(metas)

    @staticmethod
    async def _get_meta_from_folder(article_folder):
        filename = article_folder.joinpath(conf.META_FILE_NAME)
        logger.info(f"Getting meta from {filename}")
        async with async_open(filename, "r") as f:
            meta_data = await f.read()
            js_data = json.loads(meta_data)
        return ArticleMeta(**js_data)
