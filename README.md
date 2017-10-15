# DeepBird
DeepBird is a completely automated Recurrent Neural Network and twitter bot! My goal is to make it easier to create autonomous and intelligent Twitter bots.

### To Do List:
* Make DeepBird easier to use.
* Write Docs.
* Make this more modular.
* Add Sentience Mode (Tweets and evaluates over CPU, endless Training over GPU.)
* Use a json based config file, to allow tweaking of setting while server is running.
* Clean up the code.
* Add the ability to create profiles and assign a specific model.

## Requirements:
* python 3.6.x or newer.
* Tensorflow 1.1.0rc0 (GPU version recommended).
* Tweepy.
* Datetime.
* Word-RNN (You can also use Char-RNN).
* Twitter account with an app attached to it.

### Optional, but recommended:
* Google sheet with twitter archiver enabled. (To record all tweets made by the account.)

## Basic Usage
To train with default parameters on the tinyshakespeare corpus, run:
`python train.py `

To sample from a trained model

`python sample.py`

To pick using beam search, use the --pick parameter. Beam search can be further customized using the --width parameter, which sets the number of beams to search with. For example:

`python sample.py --pick 2 --width 4`

## Automated Usage (Launch TwitterBot)
After you configure the bot in `TwitterBot.py` open a cmd, or terminal and run:
`python Twitterbot.py`