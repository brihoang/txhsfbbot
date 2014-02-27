import tweepy
from tweepy.streaming import StreamListener

class StdOutListener(StreamListener):
	def on_status(self, status):
		print status.user.screen_name
		print status.text 
		return True

	def on_error(self, status):
		return True

c_key = withheld
c_secret = witheld 

access_token = withheld  
access_token_secret = withheld 

l = StdOutListener()
auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(access_token, access_token_secret)
stream = tweepy.Stream(auth, l)
stream.filter(track=['dawson football'])
