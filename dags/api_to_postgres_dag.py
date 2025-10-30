from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import psycopg2

# ---------------------------
# Default DAG arguments
# ---------------------------
default_args = {
    "owner": "lenny",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "depends_on_past": False
}

# ---------------------------
# DAG definition
# ---------------------------
with DAG(
    dag_id="api_to_postgres_dag",
    default_args=default_args,
    description="ETL pipeline: extract data from API, transform, and load to Postgres",
    schedule_interval="@daily",  # runs every day at midnight
    start_date=datetime(2025, 10, 1),
    catchup=False,
    tags=["ETL", "API", "Postgres"],
) as dag:

    # ---------------------------
    # Task 1: Extract data from API exmaple API : https://jsonplaceholder.typicode.com/users
    # ---------------------------
    def extract_data():
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv("/tmp/api_raw_data.csv", index=False)
        print("✅ Extracted and saved raw data.")
    
    extract_task = PythonOperator(
        task_id="extract_api_data",
        python_callable=extract_data
    )

    # ---------------------------
    # Task 2: Transform data
    # ---------------------------
    def transform_data():
        df = pd.read_csv("/tmp/api_raw_data.csv")
        # Example: select only name, email, city
        df = df[["name", "email", "address.city"]].rename(columns={"address.city": "city"})
        df.to_csv("/tmp/api_clean_data.csv", index=False)
        print("✅ Transformed data and saved cleaned CSV.")

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    # ---------------------------
    # Task 3: Load data into PostgreSQL
    # ---------------------------
    def load_data():
        df = pd.read_csv("/tmp/api_clean_data.csv")
        conn = psycopg2.connect(
            host="localhost",
            dbname="airflowdb",
            user="airflow",
            password="airflow"
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS api_users (
                name TEXT,
                email TEXT,
                city TEXT
            )
        """)
        for _, row in df.iterrows():
            cur.execute("INSERT INTO api_users (name, email, city) VALUES (%s, %s, %s)",
                        (row["name"], row["email"], row["city"]))
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Loaded data into PostgreSQL table.")

    load_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=load_data
    )

    # ---------------------------
    # Set task dependencies
    # ---------------------------
    extract_task >> transform_task >> load_task