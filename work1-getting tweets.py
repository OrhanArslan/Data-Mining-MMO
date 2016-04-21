import tweepy

consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

user = raw_input("Please enter the twitter username: ")
stuff = api.user_timeline(screen_name = user, count = 100, include_rts = True)
for status in stuff:
    print (status.text, status.created_at, status.id, status.place)
