from sqlalchemy import Column, String, Integer, TIMESTAMP
from database import base


class cleanbooks(base):
    __tablename__ = "clean_books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    stars = Column(String)
    stock = Column(String)
    category = Column(String)
    book_tax = Column(String)
    number_reviews = Column(String)
    page_url = Column(String)
    loaded_at = Column(TIMESTAMP)

