# 🐾 Animal-Shelter-ETL-Pipeline
An ETL pipeline built with **Apache Airflow**, **Python**, **MongoDB**, and **Redis** using real animal shelter outcome data from the Austin Animal Center.

---

## 📁 Project Structure

```
COMMONANIMALBREEDSANDOUTCOMES/
├── dags/
│   └── animals_pipeline_dags.py
├── data/
│   └── Austin_Animal_Center_Outcomes.csv
├── scripts/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load_to_mongo.py
│   ├── load_to_redis.py
│   └── telegram_alert.py
├── .gitignore
├── airflow.cfg
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Overview

The DAG `animal_pipeline_dag` runs four tasks in sequence:

```
extract → transform → load_to_mongodb → load_to_redis
```

| Task | Description |
|---|---|
| `extract` | Reads the CSV file into memory |
| `transform` | Cleans dates, normalizes fields, drops nulls |
| `load_to_mongodb` | Inserts cleaned records into `my-database.animal_shelter` |
| `load_to_redis` | Caches avg shelter stay and total adoptions as Redis keys |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Apache Airflow 3.2.1 | Pipeline orchestration |
| Python / pandas | Data extraction and transformation |
| MongoDB | Document store for animal records |
| Redis | Cache layer for aggregated stats |

---

## 📦 Requirements

```
pandas==2.3.2
pymongo==4.17.0
redis==7.4.0
```

## 🚀 Running the Pipeline

All services run via Docker. Trigger the DAG from the Airflow UI at `http://localhost:8080`.
