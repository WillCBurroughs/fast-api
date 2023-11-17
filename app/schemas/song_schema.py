from typing import Optional

from pydantic import BaseModel

class Song(BaseModel):
    id: int
    title: str
    album_id: int

