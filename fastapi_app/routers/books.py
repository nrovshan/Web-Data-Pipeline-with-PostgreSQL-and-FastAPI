from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app.database import get_db  
from fastapi_app.db_models import CleanBooks

router = APIRouter()




@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(CleanBooks).all()


@router.get("/books/search")
def search_books(title: str, db: Session = Depends(get_db)):
    book = db.query(CleanBooks).filter(CleanBooks.title.ilike(f"%{title}%")).all()
    
    if not book:
        raise HTTPException(status_code=404, detail="No books found with that title")
    return book

