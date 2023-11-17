from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "UserList"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, default="Name")

    # Define relationships
    ListenerPlaylist = relationship("ListenerPlaylist", back_populates="UserList")

    def __repr__(self) -> str:
        return f"Song(id={self.id!r}, name = {self.name!r})"