from sqlalchemy.orm import Session
from src.model.all_models import FileMetadata

def create_file_metadata(db: Session, filename: str, filetype: str, filesize: int):
    db_file = FileMetadata(filename=filename, filetype=filetype, filesize=filesize)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_files(db: Session):
    return db.query(FileMetadata).all()
