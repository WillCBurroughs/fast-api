from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class Artist(Base):
    __tablename__ = "ArtistList"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, default="Name")

    # Define relationships
    AlbumArtists = relationship("AlbumArtists", back_populates="Artist")
    SongArtists = relationship("SongArtists", back_populates="Artist")

    def __repr__(self) -> str:
        return f"Artist(id={self.id!r}, title={self.title!r})"