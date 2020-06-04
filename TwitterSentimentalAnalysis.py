from textblob import TextBlob
import tweepy


def connectAPI(word):
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	public_tweets = api.search(word)
	return public_tweets

def iteration(public_tweets):
	avgPolarity = 0.0
	count = 1
	for tweets in public_tweets:
		avgPolarity = avgPolarity + TextBlob(tweets.text).sentiment.polarity
		count = count + 1
	score = avgPolarity/count
	return(score)


word = input("Enter the phrase for sentimental analysis : ")
public_tweets = connectAPI(word)
score = iteration(public_tweets)
print(score)
