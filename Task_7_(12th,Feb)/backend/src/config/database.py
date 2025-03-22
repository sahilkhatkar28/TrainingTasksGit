from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base,Session

DATABASE_URL = "sqlite:///./task7.db"  # Change to MySQL if needed

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()