import pymongo
from pymongo import MongoClient
import requests


url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

lingo_list = ['en', 'fa', 'es', 'fr', 'zh', 'de', 'ar', 'hi', 'tr', 'la' ]


headers = {
'accept-encoding': "application/gzip",
'x-rapidapi-host': "google-translate1.p.rapidapi.com",
'x-rapidapi-key': "fd54efecdbmshc2b9f734e39e292p1b2bdejsn14a62b37e3c9"
}

for i in lingo_list:
querystring = {"target": i }
respond = requests.request("GET", url, headers=headers, params=querystring).json()["data"]["languages"]


try:
connect = MongoClient()
print("Successfully Connect to Mongodb.")

except:
print("Can not connect to Mongodb.")

db = connect.apiLanguages2
collection = db.LanguagesData

for k in respond:
print(k)
collection.insert_one(k)

cursor = collection.find()

for data in cursor:
print(data)

cursor1 = collection.find({}, {"language":1})

for data in cursor1:
print(data)
