from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from book_scrape import scrape_pages
from datetime import datetime


# Function to create the `books` table in PostgreSQL if it doesn't exist
def create_table():

    # Initialize a connection to PostgreSQL using Airflow hook
    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()

    # Create table if it doesn't already exist
    cursor.execute("""
        Create table if not exists books (
                   id serial primary key,
                   title text,
                   price text,
                   stars text,
                   stock text,
                   loaded_at timestamp);
                   """)


    # Commit the transaction and close connection
    conn.commit()
    cursor.close()
    conn.close()


# Function to insert scraped book data into the `books` table
def insert_table(start_page: int, end_page: int):
    hook = PostgresHook(postgres_conn_id = "my_postgres_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()


    # Scrape book data from the given page range
    books = scrape_pages(start_page, end_page) 


    # Insert each book into the table
    for book in books:
        
        cursor.execute(
            "INSERT INTO books (title, price, stars, stock, loaded_at) VALUES (%s, %s, %s, %s, %s)",
            (*book, datetime.now())
    )
        

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()



# Define the DAG
with DAG(
    dag_id="scrape_and_store_books",
    start_date=datetime(2025, 7, 13),
    schedule_interval=None,
    catchup=False,
    tags=["scraping", "postgres"],
) as dag:


    # Task to create the books table
    create_table_task = PythonOperator(
            task_id="create_table",
            python_callable=create_table
        )


    # Loop to create multiple scraping tasks (5 batches of 10 pages = 50 pages total)
    for i in range(5):
        start = i * 10 + 1
        end = (i + 1) * 10

        # Define a scraping and insertion task for each batch
        scrape_task = PythonOperator(
            task_id=f"scrape_pages_{start}_{end}",
            python_callable=insert_table,
            op_args=[start, end]
            )
        
    

    run_dbt = BashOperator(
        task_id = "transformation_stage",
        bash_command = "cd C:/Users/Narmin/Desktop/auto_pipe_project/dbt_transform && dbt run",
        dag = dag )

    create_table_task >> scrape_task >> run_dbt

