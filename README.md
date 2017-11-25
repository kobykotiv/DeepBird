# DeepBird: The smartest bird in the nest!
DeepBird is a completely automated Recurrent Neural Network and Twitter bot! My goal is to make it easier to create autonomous and intelligent Twitter bots. Mostly recycled code from [Word-RNN]($https://github.com/hunkim/word-rnn-tensorflow$) and [Char-RNN]($https://github.com/sherjilozair/char-rnn-tensorflow$)

---
### To Do List:
* Make DeepBird easier to use.
* Write Documentation.
* Make this more modular.
* Add Synergy Mode (Tweets and evaluates over CPU, endless Training over GPU.)

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
* Create a New profile!
 `python3 DeepBirdWizard.py`

* Start Training
`python3 DeepBird.py --profile_dir` *PROFILE_DIR* `--train 1`

* Start Running
`python3 DeepBird.py --profile_dir` *PROFILE_DIR* `--rly_post` *BOOL* `--debug` *BOOL*
---
## Currently Deployed
[@KaleBobRoss](https://twitter.com/KaleBobRoss) is a simple Word-RNN trained on the transcripts from [Bob Ross: The Joy Of Painting](https://www.youtube.com/playlist?list=PLAEQD0ULngi67rwmhrkNjMZKvyCReqDV4). @KaleBobRoss even has a [spreadsheet archive](https://goo.gl/L57xiP).