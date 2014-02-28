import tweepy

from tweepy.streaming import StreamListener
from auth import authorize

teamAName = "Dawson"
teamBName = "Friendswood"
teamAScore = 0
teamBScore = 0
verified_A_score = 0
verified_B_score = 0
possible_scores = {}



def VERIFICATION_RESET():
	return 3

def verify():
	global possible_scores
	global teamAScore
	global teamBScore
	for k in possible_scores.iterkeys():
		if possible_scores[k] >= VERIFICATION_RESET():
			teamAScore = k[0] 
			teamBScore = k[1]
			possible_scores.clear()
			printScore()
			break

def processScore(game_info):
	global possible_scores
	words = game_info.split()
	for x in range(len(words)):
		if words[x].lower() == teamAName.lower():
			teamA = words[x+1]
		elif words[x].lower() == teamBName.lower():
			teamB = words[x+1]
	tup = (teamA, teamB)
	if tup not in possible_scores.keys() and (teamA != teamAScore or teamBScore != teamBScore):
		possible_scores[tup] = 0
	if tup in possible_scores: 
		possible_scores[tup] += 1
	verify()

def printScore():
	print teamAName + " " + str(verified_A_score)
	print teamBName + " " + str(verified_B_score)

class StdOutListener(StreamListener):
	def on_status(self, status):
		tweet = status.text
		if teamAName.lower() in tweet.lower() and teamBName.lower() in tweet.lower():
			processScore(tweet)
		return True

	def on_error(self, status):
		return True

l = StdOutListener()
auth = authorize() 

stream = tweepy.Stream(auth, l)
stream.filter(track=['dawson'])
