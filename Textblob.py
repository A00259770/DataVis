from twitter_auth import *
import tweepy as tp
import re
from textblob import TextBlob
import pandas as pd


def order_tweet(clean):
    return re.sub('[^A-Za-z0-9 ]+', '', clean)


def get_blob_tweets(query):
    auth = tp.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tp.API(auth)
    tweets = {}
    text = TextBlob
    tweets_from_api = api.search(q=query)
    id = 0
    for tweet in tweets_from_api:
        tweets[id] = {
            'id': id,
            'username': tweet.user.name,
            'text': order_tweet(tweet.text),
            'sentiment': text(tweet.text).polarity
        }
        id += 1
    df = pd.DataFrame.from_dict(tweets, orient='index')
    df.set_index('id', inplace=True)
    df.to_csv('output1.csv')
    return df


if __name__ == '__main__':
    get_blob_tweets()
