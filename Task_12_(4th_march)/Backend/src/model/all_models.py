from sqlalchemy import Column, Integer, String
from src.config.database import Base

class FileMetadata(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    filetype = Column(String)
    filesize = Column(Integer)
