import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
  'owner': 'zainab',
  'depends_on_past': True,
  'retries': 1,
  'retry_delay': timedelta(minutes=10),
  }


dag_start_stop_commands = DAG(
  'dag_start_stop_commands',
  default_args=default_args,
  schedule_interval=timedelta(minutes=15),
  start_date=datetime(2022, 1, 20),
  description='execute start and stop commands ',
  )

start_hadoop = BashOperator(
  task_id="start_task",
  bash_command="start-all.sh ",
  dag=dag_start_stop_commands
  )

start_spark = BashOperator(
  task_id="start_spark",
  bash_command="pyspark ",
  dag=dag_start_stop_commands,
  run_as_user='zainab'
  )

# print("creating a directory")
  cd_kafka_home = BashOperator(
  task_id="cd_kafka_home",
  bash_command="cd /home/zeinab/opt/kafka_2.3.1 ",
  do_xcom_push=True,
  dag=dag_start_stop_commands,
  run_as_user='zainab'
  )
  
start_zookeeper = BashOperator(
  task_id="start_zookeeper",
  bash_command="bin/zookeeper-server-start.sh config/zookeeper.properties ",
  do_xcom_push=True,
  dag=dag_start_stop_commands,
  run_as_user='zainab'
  )

start_kafka_server = BashOperator(
  task_id="start_kafka_server",
  bash_command="bin/kafka-server-start.sh config/server.properties ",
  do_xcom_push=True,
  dag=dag_start_stop_commands,
  run_as_user='zainab'
  )

start_hadoop>>start_spark>>cd_kafka_home>>[start_zookeeper, start_kafka_server]


if __name__ == '__main__ ':
dag_start_stop_commands.cli()
