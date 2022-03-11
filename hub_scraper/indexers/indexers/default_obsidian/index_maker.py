import asyncio

from pprint import pprint

from aiofile import async_open
from loguru import logger

from hub_scraper import conf
from hub_scraper.indexers.indexer import Indexer

from .models import Metas, Tag


class DefaultObsidian(Indexer):
    async def make_index(self):
        meta_data = await self._get_metas()
        sorted_metas = meta_data.sort_by_tags()
        sorted_tags = sorted(list(sorted_metas.keys()))

        tasks = [self._save_table(tag, sorted_metas[tag]) for tag in sorted_tags]
        await asyncio.gather(*tasks)

    async def _get_metas(self) -> Metas:
        article_folders = self.data_folder.get_article_folders()
        metas = await Metas.from_folders(article_folders)
        return metas

    async def _save_table(self, tag: Tag, metas: Metas):
        logger.info(f"Saving index for {tag}")
        filepath = self.data_folder.index_folder.joinpath(tag.filename)
        async with async_open(filepath, "w") as f:
            await f.write(f"# {tag.name}\n")

            for meta in metas:
                filepath = (
                    f"../{conf.ARTICLES_FOLDER_NAME}/{meta.id}/{conf.ARTICLE_FILE_NAME}"
                )
                line = f"- [[{filepath} | {meta.title}]]\n"
                await f.write(line)
