"""
Exercise - 01
`from airflow import DAG from airflow.operators.bash_operator import BashOperator from datetime import datetime, timedelta

take the dag we built in class and add a last task which removes the dataset_raw.txt from the source folder
default_dag_args = { 'start_date': datetime(2022, 1, 1), 'email_on_failure': False, 'email_on_retry': False, 'retries': 1, 'retry_delay': timedelta(minutes=5), 'project_id': 1 }

let's define our DAG
with DAG("First_DAG", schedule_interval = None, default_args = default_dag_args) as dag:

# here at this level we define our tasks of the DAG
task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ")
task_1 = BashOperator(task_id = 'bash_task_move_data', bash_command = "cp /Users/pedrocarneiro/peter/develhop/DATA_CENTER/DATA_LAKE/dataset_raw.txt  /Users/pedrocarneiro/peter/develhop/DATA_CENTER/CLEAN_DATA")
task_2 = BashOperator(task_id = 'bash_task_move_data', bash_command = "")


# in the end of your DAG definition, we want to write the dependencies between tasks. >> <<
task_0 >> task_1 >> task_2`
"""
# take the dag we built in class and add a last task which removes the dataset_raw.txt from the source folder

from airflow import DAG 
# from airflow.operators.bash import BashOperator 
from airflow.operators.bash_operator import BashOperator 
from datetime import datetime, timedelta

default_dag_args = { 'start_date': datetime(2022, 1, 1), 
                     'email_on_failure': False, 
                     'email_on_retry': False, 
                     'retries': 1, 
                     'retry_delay': timedelta(minutes=5), 
                     'project_id': 1 }

# let's define our DAG
with DAG("First_DAG_2", schedule_interval = None, default_args = default_dag_args) as dag:

# here at this level we define our tasks of the DAG
    task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ")
    task_1 = BashOperator(task_id = 'bash_task_move_data_1', bash_command = "cp /opt/airflow/dags/DATA_CENTER/DATA_LAKE/dataset_raw.txt /opt/airflow/dags/DATA_CENTER/CLEAN_DATA") # cp = copy command in bash
    task_2 = BashOperator(task_id = 'bash_task_move_data_2', bash_command = "rm /opt/airflow/dags/DATA_CENTER/DATA_LAKE/dataset_raw.txt")


# in the end of your DAG definition, we want to write the dependencies between tasks. >> <<
    task_0 >> task_1 >> task_2