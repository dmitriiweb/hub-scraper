import asyncio
import json
import re

from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol

import chompjs
import lxml.html as lh

from aiofile import async_open
from loguru import logger
from markdownify import markdownify


RE_SCRIPT = re.compile(r"window.__INITIAL_STATE__=(.*);")


class Response(Protocol):
    text: str
    status_code: int
    url: str


@dataclass
class Author:
    author_alias: str

    @classmethod
    def from_dict(cls, author_dict: Dict[str, Any]) -> "Author":
        return cls(author_dict["alias"])


@dataclass
class ArticleMeta:
    id: str
    url: str
    time_published: datetime
    is_corporative: bool
    lang: str
    title: str
    description: str
    author: Author
    tags: List[str]

    @property
    def tags_as_string(self) -> str:
        return ", ".join(self.tags)

    @property
    def json(self) -> str:
        as_dict = asdict(self)
        as_dict["time_published"] = self.time_published.isoformat()
        return json.dumps(as_dict, indent=4)


class Article:
    def __init__(self, meta: ArticleMeta, text_html: str, output_folder: Path):
        self.meta = meta
        self.text_html = text_html
        self.article_folder = self._get_article_folder(output_folder)

    def __repr__(self) -> str:
        return f"<Article {self.meta.title}>"

    @property
    def text_md(self) -> str:
        dt = self.meta.time_published.strftime("%Y-%m-%d %H:%M")
        title = f"[{self.meta.title}]({self.meta.url})"
        tags = self.meta.tags
        article_text = (
            f"# {title}\n**{self.meta.author.author_alias} {dt}**\n*{tags}*\n"
        )
        article_text += markdownify(self.text_html)
        return article_text

    @classmethod
    def from_response(
        cls, response: Response, articles_output_folder: Path
    ) -> Optional["Article"]:
        if response is None or response.status_code >= 400:
            return None

        html = lh.fromstring(response.text)
        script_txt = "window.__INITIAL_STATE__="
        script = html.xpath(".//script[contains(text(), '" + script_txt + "')]/text()")[
            0
        ].strip()
        js_data = RE_SCRIPT.match(script).group(1)  # type: ignore
        raw_data = chompjs.parse_js_object(js_data)
        article_data = raw_data["articlesList"]["articlesList"]
        for _, v in article_data.items():
            author = Author.from_dict(v["author"])
            tags = [tag["title"] for tag in v["hubs"]]
            meta = ArticleMeta(
                id=v["id"],
                url=str(response.url),
                time_published=datetime.strptime(
                    v["timePublished"], "%Y-%m-%dT%H:%M:%S%z"
                ),
                is_corporative=v["isCorporative"],
                lang=v["lang"],
                title=v["titleHtml"],
                description=v["leadData"]["textHtml"],
                author=author,
                tags=tags,
            )
            return cls(
                meta=meta,
                text_html=v["textHtml"],
                output_folder=articles_output_folder,
            )
        return None

    async def save(self):
        logger.info(f"Saving {self} to {self.article_folder.absolute()}")
        tasks = [self._save_article(), self._save_meta()]
        await asyncio.gather(*tasks)
        # await self._save_article()
        # await self._save_meta()

    async def _save_article(self):
        await self._save_text_data("article.md", self.text_md)

    async def _save_meta(self):
        await self._save_text_data("meta.json", self.meta.json)

    async def _save_text_data(self, filename: str, data: str):
        filepath = self.article_folder.joinpath(filename)
        async with async_open(filepath, "w") as f:
            await f.write(data)

    def _get_article_folder(self, output_folder: Path) -> Path:
        folder = output_folder.joinpath(self.meta.id)
        folder.mkdir(exist_ok=True, parents=True)
        return folder
