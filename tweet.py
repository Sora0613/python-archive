#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tweepy
import datetime
import sys

CK = ""
CS = ""
AT = ""
AS = ""

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

while True:
    tweet = input("Tweet:")
    try:
        todaydetail = datetime.datetime.today()
        time = todaydetail.strftime("[%H:%M:%S]")
        api.update_status(tweet)
        print(time + u'Done')
    except:
        sys.exit()
