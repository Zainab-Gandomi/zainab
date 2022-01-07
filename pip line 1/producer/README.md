 from time import sleep
 from json import dumps
 from kafka import KafkaProducer

 import requests

 url1 = "https://hotels4.p.rapidapi.com/locations/v2/search"

 querystring1 = {"query":"London","locale":"en_GB","currency":"GBP"}

 headers1 = {
     'x-rapidapi-host': "hotels4.p.rapidapi.com",
     'x-rapidapi-key': "fd54efecdbmshc2b9f734e39e292p1b2bdejsn14a62b37e3c9"
}

response1 = requests.request("GET", url1, headers=headers1, params=querystring1)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
        
        value_serializer=lambda x:
        
        dumps(x).encode('utf-8'))


producer.send("Best", value=response1.json())

print(response1.text)
