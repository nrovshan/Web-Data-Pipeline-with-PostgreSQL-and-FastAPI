from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = 'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}'

engine = create_engine(db_url)


Session_local = sessionmaker(bind=engine)
session = Session_local()

base = declarative_base()