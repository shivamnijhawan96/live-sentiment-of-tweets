import pandas as pd
import tweepy
import numpy as np
from credentials import *

def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()
tweets = extractor.user_timeline(screen_name="realDonaldTrump",count=200)
   
data = pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])

print(dir(tweets[0]))
data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['ID'] = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
print(data.head())

data.to_csv('tweets.csv', encoding='utf-8', index=False)
























































