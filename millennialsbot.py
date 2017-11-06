#!/usr/bin/env python3
# millennials bot test

import tweepy
import random

CONSUMER_KEY = 'wPP24Km141RsV8NcsGuXEQe4I'
CONSUMER_SECRET = 'Bl8msA4SMfjpuHrMiIJqRp27SIoOZZhtqu6aMB7BLlFmti7K0C'
ACCESS_KEY = '927237710326194176-bsTPgnshg59cmT72NGDJsw1wel84t98'
ACCESS_SECRET = 'O6dKTlUbfz79nEdnm9VjTNZTL4hynCPEmIojb953QMVe4'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

selector = random.randint(1,20)
with open("/Users/tim/Documents/MillennialsBot/nouns.txt") as f:
    lines = f.readlines()
    noun = random.choice(lines)
    noun2 = random.choice(lines)

if selector==1:
	newStatus = "Millennials are killing the " + noun.rstrip() + " industry. When will it end?"
if selector==2:
	newStatus = "First it was the " + noun.rstrip() + " industry. Now millennials are destroying the " + noun2.rstrip() + " industry"
if selector==3:
	newStatus = "Now millennials are killing the " + noun.rstrip() + " industry, new study finds"
if selector==4:
	newStatus = "'Psychologically scarred' millennials are killing off the " + noun.rstrip() + " industry"
if selector==5:
	newStatus = "The " + noun.rstrip() + " industry is getting destroyed by millennials, so now it's on Snapchat"
if selector==6:
	newStatus = "Millennials have ruined the " + noun.rstrip() + " industry. What's next? Story:"
if selector==7:
	newStatus = noun.rstrip() + " purveyors are terrified of what millennials are doing to their businesses. Now they're fighting back."
if selector==8:
	newStatus = "Millennials are saying no to " + noun.rstrip() + "-themed restaurants"
if selector==9:
	newStatus = "Millennials are destroying the " + noun.rstrip() + " industry"
if selector==10:
	newStatus = "Did millennials kill the " + noun.rstrip() + "?"
if selector==11:
	newStatus = "How millennials ruined the " + noun.rstrip() + ". Story:"
if selector==12:
	newStatus = "Don't let millennials near your " + noun.rstrip()
if selector==13:
	newStatus = "Why are millennials killing the " + noun.rstrip() + " industry?"
if selector==14:
	newStatus = "Millennials have officially ruined the " + noun.rstrip()
if selector==15:
	newStatus = "Millennials have killed " + noun.rstrip() + " programs"
if selector==16:
	newStatus = "Hypocritical millennials now ruining the " + noun.rstrip()
if selector==17:
	newStatus = "Congratulations, millennials: You've now killed off the " + noun.rstrip()
if selector==18:
	newStatus = "Will millennials kill the " + noun.rstrip() + " industry?"	
if selector==19:
	newStatus = "What's next for bloodthirsty millennials? The " + noun.rstrip() + " and " + noun2.rstrip() + " industries"
if selector==20:
	newStatus = "Millennials are killing the " + noun.rstrip() + " industry. MY COLUMN:"	
		    
api.update_status(newStatus)