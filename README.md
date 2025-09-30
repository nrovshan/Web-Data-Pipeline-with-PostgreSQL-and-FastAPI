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

## Project Goal

The goal of this project is to design and implement a **complete, production-style data pipeline** that demonstrates how to:

1. **Extract** structured data from an external source (in this case, a public e-commerce/book website — used here only as an example; the same approach can be applied to any HTML/JSON API source such as product catalogs, news portals, or job boards).
2. **Ingest** and **orchestrate** the extraction process using **Apache Airflow**, ensuring automation, scheduling, and monitoring of data workflows.
3. **Store raw data** in a **PostgreSQL** database for persistence and reproducibility.
4. **Transform** raw data into a clean, analytics-ready format using **dbt**, following best practices for modular SQL modeling.
5. **Serve** the cleaned data through a **FastAPI** REST interface, enabling integration with other systems or easy data exploration.
6. **Monitor and visualize** pipeline performance using an **observability stack**:
   - **StatsD Exporter**: Collects Airflow’s operational metrics.
   - **Prometheus**: Pulls metrics in Prometheus exposition format for time-series storage.
   - **Grafana**: Visualizes DAG run durations, task success/failure rates, and scheduler health through interactive dashboards.


## Manual Build

``` 1. Clone env.example file
cp .env.example .env