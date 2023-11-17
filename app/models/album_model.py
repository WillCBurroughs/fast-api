from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel

class Album(Base):
    __tablename__ = "AlbumList"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, default="Name")

    # Define relationships
    AlbumArtists = relationship("AlbumArtists", back_populates="Albums")
    Song = relationship("Song", back_populates="Albums")

    def __repr__(self) -> str:
        return f"Album(id={self.id!r}, title={self.title!r})"

class AlbumCreate(BaseModel):
    title: str

    class Config:
        orm_mode = True

