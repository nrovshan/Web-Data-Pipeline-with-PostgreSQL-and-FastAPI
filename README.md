# Web Data Pipeline — Web Scraping, Airflow, PostgreSQL, dbt, FastAPI

![Project Architecure:](screenshots/project_architecture.png)



## Overview

This project is an **end-to-end data pipeline** that:
1. Scrapes book data from [Books to Scrape](https://books.toscrape.com/).
2. Loads raw data into **PostgreSQL** via **Apache Airflow**.
3. Cleans and transforms data with **dbt**.
4. Exposes processed data through a **FastAPI REST API**.

The goal is to demonstrate **ETL orchestration**, **SQL transformations**, and **API integration** in a real-world workflow.

---

## Tech Stack

| Tool         | Purpose |
|--------------|---------|
| **Python**   | Web scraping, ETL tasks |
| **BeautifulSoup4** | HTML parsing |
| **PostgreSQL** | Raw & cleaned data storage |
| **Apache Airflow** | DAG orchestration |
| **dbt-core** | Data transformations |
| **FastAPI**  | REST API for serving data |
| **Docker**   | Containerized environment |

---

## Project Structure

```plaintext
.
├── airflow_dags/
│   ├── scrape_books_dag.py        # Orchestrates scraping and DB load
│   ├── utils/                     # Helper functions
│
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   │   └── clean_books.sql    # Transformation logic
│   │   └── schema.yml
│
├── fastapi_app/
│   ├── main.py                    # API endpoints
│   ├── routers/                   # API route modules
│
├── requirements.txt
├── docker-compose.yml
├── README.md
└── docs/
    └── architecture_diagram.png
