from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from book_scrape import scrape_pages
from datetime import datetime


def create_table():
    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        Create table if not exists books (
                   id serial primary key,
                   title text,
                   price text,
                   stars text,
                   stock text);
                   """)

    conn.commit()
    cursor.close()
    conn.close()



def insert_table(start_page: int, end_page: int):
    hook = PostgresHook(postgres_conn_id = "my_postgres_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()

    books = scrape_pages(start_page, end_page) 

    for book in books:
        
        cursor.execute(
            "INSERT INTO books (title, price, stars, stock) VALUES (%s, %s, %s, %s)",
            book
    )
        
    conn.commit()
    cursor.close()
    conn.close()


with DAG(
    dag_id="scrape_and_store_books",
    start_date=datetime(2025, 7, 13),
    schedule_interval=None,
    catchup=False,
    tags=["scraping", "postgres"],
) as dag:

    create_table_task = PythonOperator(
            task_id="create_table",
            python_callable=create_table
        )

    for i in range(5):
        start = i * 10 + 1
        end = (i + 1) * 10
        scrape_task = PythonOperator(
            task_id=f"scrape_pages_{start}_{end}",
            python_callable=insert_table,
            op_args=[start, end]
            )
        

    create_table_task >> scrape_task

