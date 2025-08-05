from fastapi import FastAPI
from fastapi_app.routers import books

app = FastAPI()

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "FastAPI + Airflow + PostgreSQL project"}