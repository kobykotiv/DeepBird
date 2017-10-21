# DeepBird: The smartest bird in the nest!
DeepBird is a completely automated Recurrent Neural Network and Twitter bot! My goal is to make it easier to create autonomous and intelligent Twitter bots. Mostly recycled code from [Word-RNN]($https://github.com/hunkim/word-rnn-tensorflow$) and [Char-RNN]($https://github.com/sherjilozair/char-rnn-tensorflow$)

---
### To Do List:
* Make DeepBird easier to use.
* Write Documentation.
* Make this more modular.
* Add Synergy Mode (Tweets and evaluates over CPU, endless Training over GPU.)
* Use a json or py based config file, to allow tweaking of settings while server is running. So there is no need to restart the server to make changes.
* Clean up the code. Make it pretty.
* Add the ability to create profiles and assign a specific model to the respective profile.

## Requirements:
* python 3.6.x or newer.
* Tensorflow 1.1.0rc0 (GPU version recommended).
* Tweepy.
* Word-RNN (You can also use Char-RNN).
* Twitter account with an app attached to it.

### Optional, but recommended:
* Google sheet with twitter archiver enabled. (To record all tweets made by the account.)

---

## Basic Usage
#### Using Word-RNN
To train with default parameters on the tinyshakespeare corpus, run:
`python train.py `
To sample from a trained model
`python sample.py`
To pick using beam search, use the --pick parameter. Beam search can be further customized using the --width parameter, which sets the number of beams to search with. For example:
`python sample.py --pick 2 --width 4 -x` variable x = number of words to generate. (I recomend a random range between a minimum and maximum int.)
#### Using Char-RNN
To train with default parameters on the tinyshakespeare corpus, run:
`python train.py `
To sample from a trained model
`python sample.py`
To pick using beam search, use the --pick parameter. Beam search can be further customized using the --width parameter, which sets the number of beams to search with. For example:
`python sample.py --pick 4 --width 6 -n x` variable x = number of characters for each use of sample.py (I recomend a random range between a minimum and maximum int.)

---
## Automated Usage (Launch TwitterBot)
After you configure the bot in `TwitterBot.py` open a cmd, or terminal and run:
`python Twitterbot.py`

---
## Currently Deployed
[@KaleBobRoss](https://twitter.com/KaleBobRoss) is a simple Word-RNN trained on the transcripts from [Bob Ross: The Joy Of Painting](https://www.youtube.com/playlist?list=PLAEQD0ULngi67rwmhrkNjMZKvyCReqDV4). @KaleBobRoss even has a [spreadsheet archive](https://goo.gl/L57xiP).