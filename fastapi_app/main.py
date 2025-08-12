from fastapi import FastAPI
from fastapi_app.routers import books, dag_trigger

app = FastAPI()

app.include_router(books.router)
app.include_router(dag_trigger.router)


@app.get("/")
def root():
    return {"message": "FastAPI + Airflow + PostgreSQL project"}

