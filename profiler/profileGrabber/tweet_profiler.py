#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "LYVbkF2Ej4KcMbwZLw9C6d2cP"
consumer_secret = "ocRn9uDoEJ8dBrUjGRrWSb1rHUvFY9ENajpfVySakw8Jz6wWVf"
access_key = "831660289418522625-BhxreR7mc1PQTsTXkSd0urfHNC63hFA"
access_secret = "4NQXUft4qaMHbGLVi7qiLklxllcSU2kodqvxwFza1fPdr"

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user used to help build function
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken" #in case of invalid screen name#

    return user_profile

# uses the function to query a Twitter user. I am testing the code on Donald Trumps's twitter feed#

s = get_profile("realDonaldTrump")

def get_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	new_tweets = api.user_timeline(screen_name = screen_name,count=10)
  	#print tweet.id, " : ", tweet.text
  	return new_tweets

