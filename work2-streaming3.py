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
class MyListener(StreamListener):

    def on_status(self, status):
        try:
            print(status.text)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['python'], async=True)