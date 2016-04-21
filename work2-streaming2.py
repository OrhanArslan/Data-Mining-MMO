import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

file = open('stream2.json', 'a')

class MyStreamListener(StreamListener):

    def on_status(self, status):
        print(status.text)
    def on_data(self, raw_data):
        print(raw_data.text)
        json_data = json.loads(raw_data)
        file.write(str(json_data))

myStreamListener=MyStreamListener()
twitter_stream = Stream(auth=api.auth, listener=MyStreamListener())
twitter_stream.filter(track=['curry'],async=True) ##(['#python'],async=True)