# 🐾 Common Animal Breeds and Outcomes — ETL Pipeline

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

Install dependencies:

```bash
pip install -r requirements.txt
```

> `apache-airflow` is expected to already be installed in your environment.

---

## 🚀 Running the Pipeline

**1. Start Airflow (standalone)**

```bash
airflow standalone
```

**2. Open the Airflow UI**

Go to `http://localhost:8080` and log in using the credentials from `simple_auth_manager_passwords.json.generated`.

**3. Trigger the DAG**

Find `animal_pipeline_dag` in the UI and click **Trigger DAG**, or run:

```bash
airflow dags trigger animal_pipeline_dag
```

---

## 🗄️ MongoDB

- **Host:** `192.168.64.1:27017`
- **Database:** `my-database`
- **Collection:** `animal_shelter`

Records are inserted after the transform step. Each document represents one animal outcome.

---

## ⚡ Redis

- **Host:** `192.168.64.1:6379`
- **DB:** `1`

Two keys are cached after the MongoDB load:

| Key | Value |
|---|---|
| `avg_stay` | Average days in shelter (float) |
| `total_adoptions` | Count of adopted animals (int) |

---

## 🔔 Failure Alerts

If any task fails, `telegram_alert.py` is triggered via the `on_failure_callback` set in `default_args`. Make sure your Telegram bot token and chat ID are configured inside that script.

---

## 📊 Dataset

**Austin Animal Center Outcomes**
- ~22,800 records
- Fields include: `Animal ID`, `Name`, `Outcome Status`, `Type`, `Primary Breed`, `Days in Shelter`, `Intake Date`, `Outcome Date`, and more.