from sqlalchemy import create_engine
from sqlalchemy.ext.declerative import declerative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'sqlite;///inventory.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False,autoflush = False,bind=engine)
Base = declerative_base()