import sys
import tweepy
import json

consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
file = open('today.json', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):
        json_data = json.loads(data)
        file.write(str(json_data))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['python'])