from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.album_model import Album, AlbumCreate
from app.schemas.album_schema import AlbumBase
from app.controllers.album_controller import *
from database import get_db

router = APIRouter(prefix="/albums")

@router.get("/", response_model=List[AlbumBase]) 
def get_albums(db: Session = Depends(get_db)):
    albums_list = crud.get_Album_list(db)
    return albums_list

@router.get("/{album_id}", response_model=AlbumBase)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.post("/", response_model=AlbumBase)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album
