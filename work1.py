import tweepy
from tweepy import OAuthHandler
import json
consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
def process_or_store(tweet):
    print(json.dumps(tweet))
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)