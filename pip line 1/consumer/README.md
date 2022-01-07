from kafka import KafkaConsumer

import pydoop.hdfs as hdfs

from json import loads


consumer = KafkaConsumer('Best', bootstrap_servers="localhost:9092",
     auto_offset_reset='earliest', enable_auto_commit=True, 
     auto_commit_interval_ms=1000, group_id='metanauts', value_deserializer=lambda 
     x:loads(x.decode('utf-8')))

hdfs_path = 'hdfs://localhost:9000/Holiday/holiday.txt'

for message in consumer:
     
     values = message.value
     with hdfs.open(hdfs_path, 'at') as f:
          f.write(f"{values}\n")

