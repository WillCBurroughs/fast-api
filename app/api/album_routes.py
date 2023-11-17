from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Album, AlbumCreate

router = APIRouter(prefix="/albums")

@router.get("/", response_model=List[Album])
def get_albums(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Album).offset(skip).limit(limit).all()

@router.get("/{album_id}", response_model=Album)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.post("/", response_model=Album)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album