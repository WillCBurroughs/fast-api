from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class Song(Base):
    __tablename__ = "SongList"

    id: int = Column(Integer, primary_key=True, index=True)
    album_id: int = Column(Integer)
    title: str = Column(String, default="Name")

    # Define relationships
    PlaylistSongs = relationship("PlaylistSongs", back_populates="SongList")
    SongArtists = relationship("SongArtists", back_populates="SongList")
    Album = relationship("Album", back_populates="SongList")

    def __repr__(self) -> str:
        return f"Song(id={self.id!r}, album_id={self.album_id!r}, title = {self.title!r})"