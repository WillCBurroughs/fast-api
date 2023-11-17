from typing import Optional

from pydantic import BaseModel

class Album(BaseModel):
    id: int
    name: str 

