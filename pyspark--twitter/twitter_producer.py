import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaConsumer
import time


access_token = "  "
access_token_secret = "   "
consumer_key = "   "
consumer_secret = "    "

#creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#setting access token
auth.set_access_token(access_token, access_token_secret)

#creating the API object by passing in auth information
api = tweepy.API(auth)

 

from datetime import datetime

def normalize_timestmp(time):
mytime = datatime.strptime(time, "%Y-%m-%d %H:%M:%S")
mytime.strftime( "%Y-%m-%d %H:%M:%S")

 

producer = KafkaProducer(bootstrap_servers ="localhost:9092")
topic_name = 'Twitter'

def get_twitter_data():
key_words = api.search_tweets(q = "covid", lang ="en")
for i in key_words:
record = ''
record += str(i.user.id_str)
record += ';'
record += str(normalize_timestamp(str(i.create_at)))
record += ';'
record += str(i.user.followrs_count)
record += ';'
record += str(i.user.location)
record += ';'
record += str(i.favorate_count)
record += ';'
record += str(i.retweet_count)
producer.send(topic_name, str.encode(record))

 

get_twitter_data()

def periodic_work(interval):
while True:
get_twitter_data()

time.sleep(interval)

# get data every couple of minute
periodic_work(60 * 0.1)

 
