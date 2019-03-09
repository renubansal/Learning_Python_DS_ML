from twython import Twython

APP_KEY = "put api key here"
APP_SECRET = "put api secret here"
OAUTH_TOKEN = "put access token here"
OAUTH_TOKEN_SECRET = "put access token secret here" 

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 

f = open('collected_data.txt','w')

username=raw_input("Enter username: ")
user_timeline  = twitter.get_user_timeline(screen_name=username, count = 1000)
for tweet in user_timeline:
	print >> f,tweet
f.write("\n")
