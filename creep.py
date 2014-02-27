import tweepy

from tweepy.streaming import StreamListener
from auth import authorize

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

l = StdOutListener()
auth = authorize() 
stream = tweepy.Stream(auth, l)
stream.filter(track=['dawson'])
