from sqlalchemy.orm import Session
from app.models.album_model import Album
from app.schemas.album_schema import AlbumCreate, AlbumUpdate

def get_album(db: Session, album_id: int):
    return db.query(Album).filter(Album.id == album_id).first()

def get_albums(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Album).offset(skip).limit(limit).all()

def create_album(db: Session, album: AlbumCreate):
    db_album = Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

def update_album(db: Session, album_id: int, album: AlbumUpdate):
    db_query = db.query(Album).filter(Album.id == album_id)
    if not db_query.first():
        return None
    db_query.update(album.dict(exclude_unset=True))
    db.commit()
    return db_query.first()

def delete_album(db: Session, album_id: int):
    db_query = db.query(Album).filter(Album.id == album_id)
    if not db_query.first():
        return None
    deleted_album = db_query.first()
    db_query.delete()
    db.commit()
    return deleted_album