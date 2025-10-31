# Apache Airflow ETL — API → PostgreSQL Pipeline

This project is a simple ETL (Extract, Transform, Load) workflow built with Apache Airflow and deployed using Docker Compose.
It showcases how to orchestrate daily data pipelines that extract information from an API, transform it with Python and Pandas, and load the processed data into PostgreSQL.
The purpose of this project is to serve as a case study and template for implementing ETL tasks with Airflow providing a foundation that can be extended with more complex logic depending on the API and business requirements.

## Purposes
✅ To Have a reliable, automated ETL that:
- Runs daily
- Cleans API data
- Loads it into Postgres
Once this works can:
- Replace the dummy API with your real data source
- Expand transformations
- Integrate alerts, dashboards, or other outputs

<img width="1880" height="547" alt="image" src="https://github.com/user-attachments/assets/baa3e1f6-f1c4-49e0-8eb5-7d7e1cb08253" />

## Features on this project

- 🧠 **Fully containerized** — no local Airflow installation required  
- 🔁 **Daily scheduled DAG** using Airflow Scheduler  
- 🧩 **ETL steps:**  
  1. Extract JSON from a REST API  
  2. Transform using Pandas  
  3. Load into PostgreSQL  
- 📊 **Web UI** to monitor and trigger DAGs  

## Basic Useful Commands
##  Command	
```docker compose up airflow-init /* 	Initialize DB & create admin user
docker compose up -d /*	Start Airflow & Postgres
docker compose down /*	Stop all services
docker compose logs -f /*	Stream logs
docker compose ps /*	Check container status```

## 🏗️ Architecture Overview
```
    A[API Source :  API : https://jsonplaceholder.typicode.com/users] --> B[Airflow Extract Task];
    B --> C[Transform Task (Pandas)];
    C --> D[Load Task (PostgreSQL)];
    D --> E[Data Warehouse / Reports];
	
```	
airflow-etl/
├── dags/
│   └── api_to_postgres_dag.py     # DAG Config
├── logs/                          # Airflow logs
├── docker-compose.yaml            # Docker config environment
└──requirements.txt               # Extra Python libs for DAG
```

Ref : https://airflow.apache.org/docs/apache-airflow/stable/start.html
