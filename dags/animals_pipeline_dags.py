from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def my_task():
    print("Hello from task!")

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="task_1",
        python_callable=my_task
    )