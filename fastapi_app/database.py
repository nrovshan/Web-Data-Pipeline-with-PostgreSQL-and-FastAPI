from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path



env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT= os.getenv("POSTGRES_PORT")


db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(db_url)


Session_local = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    
    db = Session_local()

    try:
        yield db
    finally:
        db.close()



