from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db  
from ..db_models import cleanbooks

router = APIRouter()

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(cleanbooks).all()
    return books

