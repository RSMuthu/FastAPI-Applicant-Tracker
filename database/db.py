### Make necessary SQLite DB configs & sqlalchemy ORM configs

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///./tracker.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    '''
    Provides database session for the database operations
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
