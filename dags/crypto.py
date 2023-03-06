from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from tasks.api_tasks import is_api_available


with DAG(dag_id="crypto", start_date=datetime(2023, 3, 1),
        schedule_interval="@daily", catchup=False) as dag:

    is_api_avaliable = PythonOperator(
        task_id="is_api_available",
        python_callable=is_api_available
    )

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS cripto (
                crypto_symbol TEXT NOT NULL,
                crypto_price TEXT NOT NULL,
                record_date TEXT NOT NULL
            )
        """
    )

    #create_table >> is_api_available