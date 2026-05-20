from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import task
from datetime import datetime
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.telegram_alert import send_telegram_alert
from scripts.extract import extract_function
from scripts.transform import transform_function
from scripts.load_to_redis import load_to_redis
from scripts.load_to_mongo import load_to_mongodb

@task.bash
def run_scala():
    java_home = '/home/airflow/.cache/coursier/arc/https/github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.19%252B10/OpenJDK17U-jdk_x64_linux_hotspot_17.0.19_10.tar.gz/jdk-17.0.19+10'
    scala = '/home/airflow/.local/share/coursier/bin/scala'
    script = '/opt/airflow/scripts/hello.scala'
    return (
        f'export JAVA_HOME="{java_home}" && '
        f'export PATH="$JAVA_HOME/bin:$PATH" && '
        f'{scala} run --server=false {script}'
    )

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
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform_function,
    )
    load_to_mongodb_task = PythonOperator(
        task_id="load_to_mongodb",
        python_callable=load_to_mongodb,
    )
    load_to_redis_task = PythonOperator(
        task_id="load_to_redis",
        python_callable=load_to_redis,
    )
    scala_task = run_scala()

extract_task >> transform_task >> load_to_mongodb_task >> load_to_redis_task >> scala_task