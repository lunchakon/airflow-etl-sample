# Apache Airflow ETL — API → PostgreSQL Pipeline
A simple **ETL (Extract, Transform, Load)** project built with **Apache Airflow** running in **Docker Compose**.  
This example demonstrates how to orchestrate daily workflows that extract data from an API, transform it using Python & Pandas, and load the results into PostgreSQL.

## 🚀 Features

- 🧠 **Fully containerized** — no local Airflow installation required  
- 🔁 **Daily scheduled DAG** using Airflow Scheduler  
- 🧩 **ETL steps:**  
  1. Extract JSON from a REST API  
  2. Transform using Pandas  
  3. Load into PostgreSQL  
- 📊 **Web UI** to monitor and trigger DAGs  
- 🛠️ Extendable for ML, analytics, or data warehouse pipelines


## 🏗️ Architecture Overview
```
graph TD;
    A[API Source] --> B[Airflow Extract Task];
    B --> C[Transform Task (Pandas)];
    C --> D[Load Task (PostgreSQL)];
    D --> E[Data Warehouse / Reports];
	
	
airflow-etl/
├── dags/
│   └── api_to_postgres_dag.py     # DAG definition
├── logs/                          # Airflow logs
├── docker-compose.yaml            # Docker environment
├── requirements.txt               # Extra Python libs for DAG
└── README.md                      # Documentation
