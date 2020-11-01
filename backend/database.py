from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
try:
    SQLALCHEMY_DATABASE_URL = "sqlite:///backend/database/jobs.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


    Base = declarative_base()
except Exception as e:
    print(str(e))
