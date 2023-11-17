from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class Playlist(Base):
    __tablename__ = "PlayList"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer)
    name: str = Column(String, default="Name")

    # Define relationships
    PlaylistSongs = relationship("PlaylistSongs", back_populates="Playlist")
    SongArtists = relationship("SongArtists", back_populates="Playlist")
    ListenerPlaylist = relationship("ListenerPlaylist", back_populates="Playlist")

    def __repr__(self) -> str:
        return f"Playlist(id={self.id!r}, user_id={self.user_id!r}, name = {self.name!r})"