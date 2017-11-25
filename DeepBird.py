import os
import sys
from datetime import datetime, timedelta
import time
import argparse

profile_folder = "./profiles/"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--profile_dir',type=str,required=True,
						help='profile directory. REQUIRED')
	parser.add_argument('--rly_post',type=bool,default=False,
						help='0 = evaluation only.\n1 = evaluation AND post to twitter. Timer optional.')
	parser.add_argument('--timer_mode',type=int,
						help='0 = Post every 10 minutes (Round clockTime)\n1 = Post every 15 minutes (Round clockTime)\n2 = Post every 20 minutes (Round clockTime).\n3=Post every 30 minutes (Round clockTime).\n4=Post every 60 minutes (Round clockTime).')
	parser.add_argument('--train',type=int,default=0,
						help='0 = Train NONE.\n1 = Train ONCE.\n2 = Train AUTOMATICALLY.')
	parser.add_argument('--debug',type=bool,default=False)
	args = parser.parse_args()
	Prep(args)

def Prep(args):
	debug = args.debug
	rlyPost = args.rly_post
	timer = args.timer_mode
	train_mode = args.train
	current_profile = args.profile_dir
	train = args.train

	from DeepBirdWizard import CheckProfile
	if train != 0:
		if CheckProfile(current_profile,True,False):
			if train == 1:
				DeepBirdTrain(current_profile)
				return 
			elif train == 2:
				try:
					while True:
						DeepBirdTrain(current_profile)
				except KeyboardInterrupt:
					print('DONE!\n\n---------------------')
					return
			else:
				print('invalid train mode entered.')
		else:
			pass
	else:
		pass
	
	if timer ==   0:
		btime = 10
	elif timer == 1:
		btime = 15
	elif timer == 2:
		btime = 20
	elif timer == 3:
		btime = 30
	elif timer == 4:
		btime = 60
	else:
		btime = False

	if CheckProfile(current_profile,True,False):
		if debug:
			BlockPrint(False)
		else: 
			BlockPrint(True)
		# print("RETURNED TRUE")
		while True:
			DeepBird(btime,current_profile,rlyPost)
		# from CountDown import countdown
	else:
		BlockPrint(False)
		# print("RETURNED FALSE")
		return

def BlockPrint(foo):
	if foo:
		sys.stdout = open(os.devnull, 'w')
	else:
		sys.stdout = sys.__stdout__

def DeepBird(post_time,profile,rlyPost):
	# print("Testing DeepBird")
	model = str(profile_folder+profile+'/')
	cfg = ProfileSettings(model)
	print(profile)
	# print(cfg)
	# a = GenerateTweet(profile)
	# new_a = EditTweet(a)
	new_a = EditTweet("""Velit aliquet sagittis. Massa massa ultricies mi quis hendrerit dolor. Dolor sit amet consectetur adipiscing elit duis tristique. Dolor magna eget est lorem. Ultrices dui sapien eget mi. Aliquet lectus proin nibh nisl condimentum id venenatis. Vitae tortor condimentum lacinia quis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Eget gravida cum sociis natoque penatibus et. Vitae auctor eu augue ut lectus arcu. Et malesuada fames ac turpis egestas maecenas. Eleifend mi in nulla posuere sollicitudin aliquam ultrices. Viverra aliquet eget sit amet tellus cras adipiscing.""") # This is the Tweet that tests this script.
	# The second new_a string is a benchmark of sorts.
	print('\nCHAR: '+str(len(new_a)))
	print('\nWORD: '+str(len(str.split(new_a))))
	print('\n'+new_a)
	if post_time:
		WaitDelta(post_time)
	PublishTweet(InitTwttr(cfg),new_a,rlyPost)
	return

def GetTime(dt, delta):
	return dt + (datetime.min - dt) % delta

def WaitDelta(i):
	now = datetime.now()
	print(now)
	posttime = GetTime(now, timedelta(minutes=i))
	print(str(posttime) + '   POSTTIME\n\n')
	while datetime.now() < posttime:
		now = datetime.now()
		print(now,end='\r')
		time.sleep(1)
	print('\nTime!')

def GenerateTweet(profile):
	# SAMPLE
	model = str(profile_folder+profile+'/')
	cfg = ProfileSettings(model)
	cmdl = str(' ./rnn.word-rnn/sample.py --save_dir ' + model + ' --pick ' + cfg[16] + ' --width ' + cfg[17] + ' -n ' + cfg[14])

	if len(cfg[15]) < 5:
		cfg[15] = ' '
	else:
		cmdl = str(cmdl + ' --prime ' + cfg[15])
	# from ./rnn.word-rnn import sample
	try:
		os.system(str('python3 ' + cmdl)) # 
		# # os.system(str('python ' + cmdl))
		with open('./rnn.word-rnn/TMPMSG.txt','r',encoding='utf8') as f:
			a = f.read()
	except OSError:
		pass
	except:
		pass
	return a

def ProfileSettings(filename):
	from configparser import ConfigParser
	config = ConfigParser()
	# with open(filename+'profile.ini','wb') as config
	config.read(filename+'profile.ini')
	# First establish the ini file as a list.
	cfg = [config.get('TWITTER', 'CONSUMER_KEY'), # 0
	config.get('TWITTER', 'CONSUMER_SECRET'), # 1
	config.get('TWITTER', 'ACCESS_TOKEN'), # 2
	config.get('TWITTER', 'ACCESS_TOKEN_SECRET'), # 3
	# TWITTER
	config.get('RNN_TRAIN_SETTINGS','RNN_SIZE'), # 4
	config.get('RNN_TRAIN_SETTINGS','INPUT_ENCODING'), # 5
	config.get('RNN_TRAIN_SETTINGS','NUM_LAYERS'), # 6
	config.get('RNN_TRAIN_SETTINGS','MODEL'), # 7
	config.get('RNN_TRAIN_SETTINGS','BATCH_SIZE'), # 8
	config.get('RNN_TRAIN_SETTINGS','SEQ_LENGTH'), # 9
	config.get('RNN_TRAIN_SETTINGS','NUM_EPOCHS'), # 10
	config.get('RNN_TRAIN_SETTINGS','LEARNING_RATE'), # 11
	config.get('RNN_TRAIN_SETTINGS','DECAY_RATE'), # 12
	config.get('RNN_TRAIN_SETTINGS','GPU_MEM'), # 13
	# RNN TRAIN
	config.get('RNN_SAMPLE_SETTINGS','N'), # 14
	config.get('RNN_SAMPLE_SETTINGS','PRIME'), # 15
	config.get('RNN_SAMPLE_SETTINGS','PICK'), # 16
	config.get('RNN_SAMPLE_SETTINGS','WIDTH'), # 17
	# RNN SAMPLE
	config.get('GET_TRAIN_DATA','RED_PILL'), # 18
	# DAMN YOU 4CHAN. (Seriously though, don't do this when it gets added to this. if you don't heed this warning, please do it for science. ._. )
	config.get('STATS','NUM_OF_TRAINS'), # 19
	config.get('STATS','NUM_OF_EVALUATIONS')] # 20

	return cfg

def EditTweet(tweet):
	# print('TWEET_LST: ' + str(str.split(tweet, '. ')))
	# x = str.split(tweet, '. ')
	x = tweet.partition('. ')[0] + '. '
	print('\nFirst Sentence: '+ x)
	if len(tweet) >= 300:
		tweet = tweet[:280]
	else:
		pass
	# print('TWEET_RAW: ' + tweet)
	if len(tweet) <= 32:
		# print(tweet)
		return False
	elif len(str.split(tweet)) <= 8:
		# print(tweet)
		return False
	elif len(x[0]) < 2:
		print('This first sentence is too damn small.')
		tweet = tweet.replace(x, '')
	if tweet[-1] != '. ':
		print('Does not end with a complete sentence.')
		while tweet[-1] != '.':
			tweet = tweet[:-1]
		else:
			pass
	else:
		print('Tweet ends with a complete sentence.')
	# str.split(tweet)
	if len(tweet) > 280:
		return False
	# else:
	# 	return tweet
	print('\n ')
	return tweet

def DeepBirdTrain(profile):
	model = str(profile_folder+profile+'/')
	cfg = ProfileSettings(model)

	cmdl = str('python3 ./rnn.word-rnn/train.py --data_dir ' + model + ' --log_dir ./rnn.word-rnn/logs/ ' + ' --input_encoding ' + cfg[5] + ' --save_dir ' + model + ' --rnn_size ' + cfg[4] + ' --batch_size ' + cfg[8] + ' --model ' + cfg[7] + ' --seq_length ' + cfg[9] + ' learning_rate ' + cfg[11] + ' --gpu_mem ' + cfg[13] + ' --decay_rate ' + cfg[12])

	z = int(cfg[19])

	if z <= 0:
		z = 1
		cmdl = str(cmdl + ' --init_from ' + model)
	z = z + 1
	
	epochs = int(cfg[10])

	from configparser import ConfigParser
	parser = ConfigParser()
	parser.read(model+'profile.ini')

	parser['STATS']['NUM_OF_TRAINS'] = str(z)

	cmdl = str(cmdl + ' --num_epochs ' + str(int(z * epochs)))

	with open(model+'profile.ini','w') as configfile:
		# f.set('STATS','NUM_OF_TRAINS',str(int(z)))
		# print(parser.get('STATS','NUM_OF_TRAINS'))
		parser.write(configfile)
		# f.write(parser)
		configfile.close()

	# os.system(cmdl)
	print(cmdl)
	print('I HAVE DONE THE TRAINING!!!')

def InitTwttr(cfg):
	import tweepy
	auth = tweepy.OAuthHandler(cfg[0], cfg[1])
	auth.set_access_token(cfg[2], cfg[3])
	return tweepy.API(auth)

def PublishTweet(api,tweetstring,rlyTweet):
	BlockPrint(False)
	print('\n\n')
	name = str('@'+api.me().screen_name)
	# print()
	print(str(datetime.now().strftime('%Y %b %d - %H:%M ')) + str(name)+" tweeted, '" + tweetstring)
	if rlyTweet:
		# api.update_status(tweetstring)
		print("\nPosting and Stuff.")
	else:
		print("\nHAHA! This was only practice! Nothing was posted!")

####################
### MAIN PROGRAM ###
####################

if __name__ == '__main__':
	main()