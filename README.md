# rjokes

Telegram bot that queries subreddit r/Jokes from Reddit (reddit.com/r/Jokes) for the best jokes of the day (can be modified) and then sends these jokes via telegram chat with a user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
sudo pip install telepot
sudo pip install praw
```
[telepot](https://github.com/nickoala/telepot) is a python framework for Telegram Bot API. This package will be used to connect to Telegram API and to communicate with users over the internet.

[praw](https://github.com/praw-dev/praw) is Python Reddit API Wrapper. This will be the main and only package to connect to Reddit's API and extract desired data.

### Installing

Nothing too complicated. The source code is written in python, so no worries.

The only thing that needs to be done before execution is the config profile. In the config profile you should fill your Reddit API details and Telegram Bot's unique API key.

For that please follow these steps

```
git clone https://github.com/thecsw/rjokes
cd rjokes
mv example.config.py config.py
nano config.py
```

Now here, you can use any text editor you like. When opening the file you will see this
```python
#This is for reddit
client_id = 'take it from your account\'s preferences'
client_secret = 'take it from your account\'s preferences'
username = 'username'
password = 'password'
user_agent = 'something'
#This is for telegram
token = 'YOUR TELEGRAM API KEY'
```