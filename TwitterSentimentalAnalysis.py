from textblob import TextBlob
import tweepy


def connectAPI(word):
	consumer_key = 'TUwuP3PWVfCjUaOvqWTmhnOgF'
	consumer_secret = 'nKJeMbQ9LpUysFrITuuGdQzT5X6cnddw5hK4Xt0yZcJcGSEKkh'
	access_token = '1259037559902154752-qrMWm6EMyI0I1e29x1E6MXRgyHSYpD'
	access_token_secret = 'YsZlB0f1Qsa5kJ93ta2AKqTkkepWJXFM1jnReaS4O4WHV'
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