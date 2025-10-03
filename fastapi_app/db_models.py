from sqlalchemy import Column, String, Integer, TIMESTAMP
from fastapi_app.database import Base


class CleanBooks(Base):
    __tablename__ = "clean_books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    currency = Column(String)
    star_rating = Column(String)
    stock = Column(String)
    category = Column(String)
    book_tax = Column(String)
    number_reviews = Column("number_reviews", String)
    page_url = Column(String)
    loaded_at = Column(TIMESTAMP)

