from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app.database import get_db  
from fastapi_app.db_models import cleanbooks

router = APIRouter()

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(cleanbooks).all()
    return books


@router.get("/books/search")
def search_books(title: str, db: Session = Depends(get_db)):
    books = db.query(cleanbooks).filter(cleanbooks.title.ilike(f"%{title}%")).all()
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found with that title")
    return books

