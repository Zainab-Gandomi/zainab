from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
from json import loads


consumer = KafkaConsumer('Twitter', bootstrap_servers="localhost:9092", auto_offset_reset='earliest', enable_auto_commit=True, auto_commit_interval_ms=1000, group_id='metanauts', value_deserializer=lambda x:loads(x.decode('utf-8')))

hdfs_path = 'hdfs://localhost:9000/CovidInfo/Covidinfo.txt'

for message in consumer:
values = message.value
print(values)
with hdfs.open(hdfs_path, 'at') as f:
f.write(f"{values}\n")
