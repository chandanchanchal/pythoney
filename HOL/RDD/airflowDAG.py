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

