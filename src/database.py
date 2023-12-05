from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import *


#SQLALCHEMY_DATABASE_URL = "sqlite:///./new-infra-api.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def check_db_connected():
    try:
        database = SessionLocal()
        database.execute(text("SELECT 1"))
        print("Database is connected (^_^)")
        return database
    except Exception as e:
        print("Looks like there is some problem in connection, see below traceback")
        raise e
