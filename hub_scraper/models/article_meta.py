import json

from datetime import datetime
from typing import List

from pydantic import BaseModel

from .article_author import Author


class ArticleMeta(BaseModel):
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
    def as_json(self) -> str:
        as_dict = self.dict()
        as_dict["time_published"] = self.time_published.isoformat()
        return json.dumps(as_dict, indent=4, ensure_ascii=False)
