import re

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Protocol

import chompjs
import html2md
import lxml.html as lh


RE_SCRIPT = re.compile(r"window.__INITIAL_STATE__=(.*);")


class Response(Protocol):
    text: str
    status_code: int
    url: str


@dataclass
class Article:
    id: str
    url: str
    time_published: datetime
    is_corporative: bool
    lang: str
    title: str
    description: str
    text_html: str

    @property
    def text_md(self) -> str:
        return html2md.convert(self.text_html)

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
            return cls(
                id=v["id"],
                url=response.url,
                time_published=datetime.strptime(
                    v["timePublished"], "%Y-%m-%dT%H:%M:%S%z"
                ),
                is_corporative=v["isCorporative"],
                lang=v["lang"],
                title=v["titleHtml"],
                description=v["leadData"]["textHtml"],
                text_html=v["textHtml"],
            )
        return None
