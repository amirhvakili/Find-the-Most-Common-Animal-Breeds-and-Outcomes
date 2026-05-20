from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.telegram_alert import send_telegram_alert
from scripts.extract import extract_function
from scripts.transform import transform_function
from scripts.load_to_redis import load_to_redis


with DAG(
    dag_id="animal_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    default_args={'owner': 'airflow', 'on_failure_callback': send_telegram_alert},
    schedule=None,
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_function,
    )
    tranform_task = PythonOperator(
        task_id="tranform",
        python_callable=transform_function,
    )
    load_to_redis_task = PythonOperator(
        task_id="load",
        python_callable=load_to_redis,
    )

extract_task >> tranform_task >> load_to_redis_task