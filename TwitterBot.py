import os
import sys
import time
import tweepy
import sample
import datetime

#!/usr/bin/env python
# -*- coding: utf-8 -*-

playMode = 2 # 0 preview mode, 1 post on timer, 2 post on timer.
timerTime = 30 # in minutes. Must be more than 5.
model_dir = "./save"


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'XxxxXxxxX'								#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'XxxxXxxxX'							#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'XxxxXxxxX'								#keep the quotes, replace this with your access token
ACCESS_SECRET = 'XxxxXxxxX'								#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():
	while True:
		i = 1
		if playMode == 0:
			while True:
				print("Preview mode 0 activated! Please wait...")
				time.sleep(timerTime * 1)
				a = "Hello World!"
				if len(a) <= 140:
					print("Pushing tweet!")
					MakeTweet(a,False,i)
				else:
					print("tweetstring is too long. Trying again...")
					main()
				i+=1
		elif playMode == 1:
			while True:
				print("Preview mode 1 activated! Please wait...")
				time.sleep(timerTime * 1)
				a = GenerateTweet()
				try: 
					numa = int(a.rindex('.') + 1)
					a = str(a[0:140])
					a = str(a[0:numa]).lower()
				except:
					pass
				print('TWEE:',a)
				print('CHAR:',len(a))
				print('WORD:',len(str.split(a)))
				if len(a) <= 140:
					print("Pushing tweet!")
					MakeTweet(a,False,i)
				else:
					print("tweetstring is too long. Trying again...")
					main()
				i+=1
		elif playMode == 2:
			while True:
				print("Post on timer mode activated! Please wait...")
				time.sleep(timerTime * 1)
				a = GenerateTweet()
				numa = int(a.rindex('.') + 1)
				a = str(a[0:140])
				a = str(a[0:numa]).lower()
				print('TWEE:',a)
				print('CHAR:',len(a))
				print('WORD:',len(str.split(a)))
				if len(a) <= 140:
					print("Pushing tweet!")
					MakeTweet(a,True,i)
				else:
					print("tweetstring is too long. Trying again...")
					main()
				time.sleep(timerTime * 60)
				i+=1
		elif playMode == 3:
			print("There isn't anything here. I have to come back to this section later.")
		else:
			print("Error! playMode must be set to either 0,1,2,3")
	# else:
	# 	print("Trying Again.")
	# 	main()

	# print("@KaleBobRoss just tweeted, '" + tweetstring + "'")
	# api.update_status(line)
	# time.sleep(900)

def MakeTweet(tweetstring,rlyTweet,i):
	currentTime = str(datetime.datetime.now())
	print(str(i),"Bot tweeted, '" + tweetstring + "' on " + currentTime)
	if rlyTweet:
		api.update_status(tweetstring)
	else:
		print("HAHA! This was only practice! Nothing was posted!")

def GenerateTweet():
	cmdl = str('--save_dir ' + model_dir + ' --pick 2 --width 4')
	os.system(str('python3 sample.py ' + cmdl))
	with open('TMPMSG.txt','r',encoding='utf8') as f:
		a = f.read()
	return a

####################
### MAIN PROGRAM ###
####################

if __name__ == '__main__':
	main()