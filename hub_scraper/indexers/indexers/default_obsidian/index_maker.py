from hub_scraper.indexers.indexer import Indexer

from .models import Metas


class DefaultObsidian(Indexer):
    async def make_index(self):
        meta_data = await self._get_metas()
        print(meta_data)

    async def _get_metas(self) -> Metas:
        article_folders = self.data_folder.get_article_folders()
        metas = await Metas.from_folders(article_folders)
        return metas
