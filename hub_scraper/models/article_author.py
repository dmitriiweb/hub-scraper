from typing import Any, Dict

from pydantic import BaseModel


class Author(BaseModel):
    alias: str
