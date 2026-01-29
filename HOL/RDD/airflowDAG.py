from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "cc_test",
    start_date = datetime(2024, 1, 1),
    schedule = "@daily" ,
    catchup = False,
) as dag:

   start = BashOperator(
      task_id = "start",
      bash_command = "echo 'Task start'"
   )

   task_a = BashOperator(
      task_id = "task_a",
      bash_command = "sleep 5 && echo 'Task A done'"
   )

   task_b = BashOperator(
      task_id = "task_b",
      bash_command = "sleep 5 && echo 'Task B done'"
   )

   end = BashOperator(
      task_id = "end",
      bash_command = "echo 'END'"
   )


############################################################################

with DAG(
    dag_id = "cc_test",
    start_date = datetime(2024, 1, 1),
    schedule = "@hourly" ,
    catchup = True,
) as dag:

   task = BashOperator(
      task_id = "print_date",
      bash_command = "date"
   )

#########################---------PTHONOPERATOR-------#######################3
from airflow.operators.python import PythonOperator

def greet():
    print("Hello from PythonOperator!")

with DAG(
    dag_id="python_operator",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    python_task = PythonOperator(
        task_id="greet_task",
        python_callable=greet
    )
###########################------Retries & Failure Handling---------############################
from datetime import timedelta

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

def fail_task():
    raise ValueError("Intentional failure")

with DAG(
    dag_id="retries_example",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    failing = PythonOperator(
        task_id="fail_task",
        python_callable=fail_task
    )

#########################################------XComs------------------################################

def push_value(ti):
    ti.xcom_push(key="number", value=10)

def pull_value(ti):
    value = ti.xcom_pull(key="number", task_ids="push_task")
    print(f"Received value: {value}")

with DAG(
    dag_id="xcom_example",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    push_task = PythonOperator(
        task_id="push_task",
        python_callable=push_value
    )

    pull_task = PythonOperator(
        task_id="pull_task",
        python_callable=pull_value
    )

    push_task >> pull_task

###########################################-------Variables--------#########################################

from airflow.models import Variable

def read_variable():
    env = Variable.get("env")
    print(f"Running in {env} environment")

with DAG(
    dag_id="variables_example",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    task = PythonOperator(
        task_id="read_variable",
        python_callable=read_variable
    )


