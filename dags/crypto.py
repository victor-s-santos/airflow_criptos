from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from tasks.api_tasks import is_api_available


with DAG(dag_id="crypto", start_date=datetime(2023, 3, 1),
        schedule_interval="@daily", catchup=False) as dag:

    is_api_avaliable = PythonOperator(
        task_id="is_api_available",
        python_callable=is_api_available
    )

    is_api_available