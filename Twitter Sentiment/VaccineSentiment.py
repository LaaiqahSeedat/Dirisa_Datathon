from textblob import TextBlob
import tweepy
import sys
import numpy
import matplotlib.pyplot as plt
import pandas

<<<<<<< HEAD
#The access tokens for the twitter semantics
APIKey="YrSJRKvvrm3c2qOsvMqEWuQFV"
APISecretKey="WScC6u0Lgof5WOtFVa2GJ9cHrs2eDmEucNquqHLQiJVrw2qu3M"
AccessToken="562992856-1oLVpZSVQA0tUbWoJlF1zDYxGXMxI1JgCxPLodIA"
AccessTokenSecret="tfzK13k6RqKoy9nTz5KiwdZky3EjFWrYMpvhqMy6tatbN"
=======
APIKey="u0MyqxdVT5JSFkd6nFTMFvzu1"
APISecretKey="39N8e25iyadcJveGTpGyBn0EW15F1d5I4azdXsUHSdsVsD8NBj"
AccessToken="562992856-tBa01zsmJIFs4aIruzDc6gM8YTVEfD5kfPANdzTg"
AccessTokenSecret="i8sIqiHFYGN2yOzfUy0yHYCig2Bk32O1Vin6tcYh76Mv1"
>>>>>>> 35a161f46fe2f1a7ad664ac6c9ca9fbb677732d4

auth_handler=tweepy.OAuthHandler(consumer_key=APIKey,consumer_secret=APISecretKey)
auth_handler.set_access_token(AccessToken,AccessTokenSecret)
api=tweepy.API(auth_handler)

search_term="vaccine"
<<<<<<< HEAD
tweet_amount=100
=======
tweet_amount=5
>>>>>>> 35a161f46fe2f1a7ad664ac6c9ca9fbb677732d4

#specify the api search, the search term and the language and limit it to the amount of tweets. until= end,since=start
tweets=tweepy.Cursor(api.search, q=search_term,geocode = '-29.152161,25.122126,533km',lang='en').items(tweet_amount)
polarity=0

positive=0
neutral=0
negative=0

for tweet in tweets:
    #print(tweet.text)
    #print(tweet.id)
    analysis= TextBlob(tweet.text)
    polarity += analysis.polarity
    #check the polarity of the tweet
    if analysis.polarity > 0:
        positive+=1
    elif analysis.polarity < 0:
        negative+=1
    else:
        neutral+=1

print(polarity)

print(f'Amount of positive tweets: {positive}')
positivePercent=positive/tweet_amount*100
print(f'Percentage of positive tweets: {positivePercent} %')
print(f'Amount of neutral tweets: {neutral}')
neutralPercent=neutral/tweet_amount*100
print(f'Percentage of neutral tweets: {neutralPercent} %')
print(f'Amount of negative tweets: {negative}')
negativePercent=negative/tweet_amount*100
print(f'Percentage of negative tweets: {negativePercent} %')