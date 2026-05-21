# 🐾 Animal-Shelter-ETL-Pipeline
An ETL pipeline built with **Apache Airflow**, **Python**, **MongoDB**, **Redis**, and a small **Scala reporting module** using Austin Animal Center outcome data.

---

## 📁 Project Structure

```
animal-shelter-etl-pipeline/
├── dags/
│   └── animals_pipeline_dags.py
├── data/
│   └── Austin_Animal_Center_Outcomes.csv
├── scripts/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load_to_mongo.py
│   ├── load_to_redis.py
│   ├── telegram_alert.py
│   └── report.scala
├── .gitignore
├── airflow.cfg
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Overview

The DAG `animal_pipeline_dag` runs five tasks in sequence:

```
extract → transform → load_to_mongodb → load_to_redis → report
```

| Task | Description |
|---|---|
| `extract` | Reads the CSV file into memory |
| `transform` | Cleans dates, normalizes fields, drops nulls |
| `load_to_mongodb` | Inserts cleaned records into `my-database.animal_shelter` |
| `load_to_redis` | Caches avg shelter stay and total adoptions as Redis keys |
| `report` | This report identifies and displays animals that spent more than 1000 days in the shelter |
| `telegram_alert` | Sends pipeline status notifications through Telegram (optional) |


---


## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Apache Airflow | Workflow orchestration |
| Python | ETL implementation |
| Pandas | Data processing and transformation |
| MongoDB | Persistent document storage |
| Redis | Fast caching layer |
| Scala | Reporting and analytics |
| Docker & Docker Compose | Containerized deployment |

---

## 📦 Requirements

```
pandas==2.3.2
pymongo==4.17.0
redis==7.4.0
```
