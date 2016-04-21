from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'w') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(consumer_key, consumer_secret)
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'],async=True)