import re

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Protocol

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
    def from_dict(cls, author_dict: dict) -> "Author":
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


@dataclass
class Article:
    meta: ArticleMeta
    text_html: str

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
    def from_response(cls, response: Response) -> Optional["Article"]:
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
                url=response.url,
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
            )
        return None

    async def save(self, output_folder: Path):
        article_folder = self._get_article_folder(output_folder)
        logger.info(f"Saving {self.title} to {article_folder.absolute()}")
        await self._save_article(article_folder)
        await self._save_meta(article_folder)

    async def _save_article(self, article_folder: Path):
        filepath = article_folder.joinpath("article.md")
        async with async_open(filepath, "w") as f:
            await f.write(self.text_md)

    async def _save_meta(self, article_folder: Path):
        pass

    def _get_article_folder(self, output_folder: Path) -> Path:
        folder = output_folder.joinpath(self.id)
        folder.mkdir(exist_ok=True, parents=True)
        return folder
