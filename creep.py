import tweepy
from tweepy.streaming import StreamListener

teamAName = "Dawson"
teamBName = "Friendswood"

def printScore(game_info):
	words = game_info.split()
	for x in range(len(words)):
		if words[x].lower() == teamAName.lower():
			teamAScore = words[x+1]
		elif words[x].lower() == teamBName.lower():
			teamBScore = words[x+1]
	print teamAName + " " + teamAScore
	print teamBName + " " + teamBScore

class StdOutListener(StreamListener):
	def on_status(self, status):
		tweet = status.text
		
		if teamAName.lower() in tweet.lower() and teamBName.lower() in tweet.lower():
			printScore(tweet)
		return True

	def on_error(self, status):
		return True

c_key = "RYfMX1jo5tYVqAnSagaxmQ"
c_secret = "VvsK1GgUd8IuFFuGRKUzWudHpLcrPlef6J585ZOkt0"

access_token = "1054281577-ohVrfLs0A65UYIfhnGhgxLKWMptgDIPrYPG6CTn"
access_token_secret = "CeCciJudoW2uFCvSWWRx2mvqhKRAxSPENNazZpXiHp1Zr"

l = StdOutListener()
auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(access_token, access_token_secret)
stream = tweepy.Stream(auth, l)
stream.filter(track=['dawson'])
