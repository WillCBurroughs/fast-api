from typing import Optional

from pydantic import BaseModel

class Playlist(BaseModel):
    id: int
    user_id: int
    name: str 

