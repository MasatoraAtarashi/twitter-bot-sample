#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
import sys
import tweepy
import re
# import codecs
from numpy.random import *
import random

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

tweets = []
text_data = open("ファイル名", "r")
for line in text_data:
  tweets.append(line)
text_data.close()

tweets_array = tweets[0].split(',')
tweet = random.choice(tweets_array).replace('\\n', '\n')
try:
    api.update_status(status=tweet)
    print('success!')
except tweepy.TweepError as e:
    print(e)    
