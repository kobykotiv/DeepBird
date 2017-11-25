import os
import sys
import tweepy
import io
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is the Config File for DeepBird.py

# Load Modules and Profiles
default_module = "rnn.word-rnn/"

profile_folder = "./profiles/"

def getusrChoice():
	TitleBar()
	# Let users know what they can do.
	print("[C]reate a new profile.")
	print("[V]erify an existing profile.")
	print("[A]bout this Wizard.")
	print("[Q]uit.")
	return input("\nWhat would you like to do? " )

def CreateNEWProfile():
	profile_name = str(input("What's the name of this new profile? "))
	dirx = (profile_folder+profile_name+'/')
	if not os.path.exists(dirx):
		os.mkdir(dirx)
		if not os.path.isdir(dirx+'data'):
			os.mkdir(dirx+'data')
			print("Created data folder.")
		if not os.path.isfile(dirx+'input.txt'):
			with open(dirx+'input.txt','w',encoding='UTF-8') as f:
				f.write('')
				f.close()
			print("Created input.txt")
		if not os.path.isfile(dirx+'profile.ini'):
			CreateNewINI(dirx+'profile.ini')

	else:
		print("That profile already exists. You need to git it a different name.")


def GetProfileList():
	Bar(True)
	print("\nDeepBird Profiles")
	dir_list = next(os.walk(profile_folder))[1]
	for index, folder in enumerate(dir_list):
		print(str(str(index)+'  |  '+str(folder)))
	# get input and choose item from the damned list.
	input_folder = int(input("\nEnter The Profile to Check: "))
	if input_folder != '':
		abc = str(dir_list[input_folder])
		Bar(True)
		CheckProfile(abc,True,True)
	else:
		print("You either didn't input anything, or you entered an invalid profile. Please try again.")
# else:
# 	CheckProfile(input_folder)

def CheckTwitterPY(filename):
	# model = str(profile_folder + filename)
	if os.path.isfile(filename):
		from configparser import ConfigParser
		config = ConfigParser()
		
		config.read(filename)
		
		cfgTW = [config.get('TWITTER', 'CONSUMER_KEY'),config.get('TWITTER', 'CONSUMER_SECRET'),config.get('TWITTER', 'ACCESS_TOKEN'),config.get('TWITTER', 'ACCESS_TOKEN_SECRET')]

		# ck  = config.get('TWITTER', 'CONSUMER_KEY')
		# cks = config.get('TWITTER', 'CONSUMER_SECRET')
		# at  = config.get('TWITTER', 'ACCESS_TOKEN')
		# ats = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')
		# # print(ck)
		# # print(cks)
		# # print(at)
		# # print(ats)

		# auth = tweepy.OAuthHandler(ck, cks)
		# auth.set_access_token(at, ats)
		auth = tweepy.OAuthHandler(cfgTW[0], cfgTW[1])
		auth.set_access_token(cfgTW[2], cfgTW[3])
		return tweepy.API(auth)
	else:
		return

def CreateNewINI(filename):
	with open(filename,"w") as f:
		f.write("""
[TWITTER]
CONSUMER_KEY = xx
CONSUMER_SECRET = xx
ACCESS_TOKEN = xx-xx
ACCESS_TOKEN_SECRET = xx-xx

[RNN_TRAIN_SETTINGS]
#COMMENTS = AFTER YOU HAVE TRAINED THIS MODEL YOU CANNOT CHANGE THE NETWORK TYPE! YOU HAVE BEEN WARNED.
RNN_SIZE = 255
INPUT_ENCODING = UTF-8
NUM_LAYERS = 2
MODEL = lstm
BATCH_SIZE = 50
SEQ_LENGTH = 25
NUM_EPOCHS = 50
LEARNING_RATE = 0.002
DECAY_RATE = 0.97
GPU_MEM = 0.75

[RNN_SAMPLE_SETTINGS]
N = 60
PRIME = 
PICK = 1
WIDTH = 4

[GET_TRAIN_DATA]
RED_PILL = False

[STATS]
NUM_OF_TRAINS = 0
NUM_OF_EVALUATIONS = 0
""")
		f.close()

def CheckProfile(folder,chkTwitter,qt): 
	model = str(profile_folder + folder + "/")
	# print("Model is " + model)
	# if os.path.isdir(model+abcde)
	Bar(qt)
	if os.path.isfile(model+'input.txt'):
		print("input.txt exists!")
		Bar(qt)
		if os.path.isfile(model+"words_vocab.pkl") and os.path.isfile(model+"data.npy") and os.path.isfile(model+"config.pkl") and os.path.isfile(model+"checkpoint"):
			print("This profile is ready for evaluation!")
			# print(model + "profile.ini")
			Bar(qt)
			if os.path.isfile(model+"profile.ini"):
				if chkTwitter:
					try:
						print(model+"profile.ini")
						tpy = CheckTwitterPY(model+"profile.ini")
						print("\nTesting Twitter.")
						# Bar(qt)
						name = str('@'+tpy.me().screen_name)
						print(str("If '"+name+"' is your twitter username, congratulations!"))
						print("Everything is set up!")
						return True
					except:
						print("This twitter account has not been properly configured. \nPlease check the profile.ini file for details.\nIf you never set up a twitter account for use with this bot, visit apps.twitter.com")
						return False
				else:
					print("Didn't check twitter. Everything is set up!")
					return True
			else:
				print("Created profile.ini")
				CreateNewINI(model+"profile.ini")
		else:
			print("You need to train this profile!")
			Bar(qt)
	else:
		print("input.txt doesn't exist. You need to create it and add some data to it.")
		Bar(qt)

def Bar(quiet):
	if quiet:
		print("====================================\n")
	elif not quiet:
		return
	else:
		return

def TitleBar():
	print("""

	 DeepBird Wizard
     _       _       _
  __(*)<  __('){  __(.)=
  \___)   \___)   \___)

		""")
	Bar(True)
	
def main():
	
	choice = ''
	while choice != 'q':	
		choice = getusrChoice().lower()
		# Respond to the user's choice.
		
		if choice == 'c':
			print("Let's Create a new profile!")
			CreateNEWProfile()
		elif choice == 'v':
			print("Let's verify an existing profile.")
			GetProfileList()
		elif choice == 'a':
			print("This is the DeepBird Wizard! You can use this script to create new profiles, or check existing ones.")
		elif choice == 'q':
			print("Goodbye.")
		else:
			print("\nError! I did not understand that answer.\n")

########
# MAIN #
########

if __name__ == '__main__':
	main()