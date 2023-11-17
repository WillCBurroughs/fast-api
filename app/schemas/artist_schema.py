from typing import Optional

from pydantic import BaseModel

class Artist(BaseModel):
    id: int
    name: str 

