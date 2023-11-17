from pydantic import BaseModel

class AlbumBase(BaseModel):
    id: int
    title: str 

    class Config:
        orm_mode = True

class AlbumCreate(BaseModel):
    title: str

    class Config:
        orm_mode = True


class AlbumUpdate(BaseModel):
    title: str

    class Config:
        orm_mode = True