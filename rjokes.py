import config
import telepot
from telepot.loop import MessageLoop
import praw
import random
import time

LIMIT = 500
jokesTitles = []
jokesTexts = []
reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

telebot = telepot.Bot(config.token)

def handle(msg):
    user_id = msg['chat']['id']
    command = msg['text']
    if command == '/joke':
        joke = random.randint(1, LIMIT-1)
        telebot.sendChatAction(user_id, 'typing')
        telebot.sendMessage(user_id, jokesTitles[joke])
        time.sleep(1)
        telebot.sendChatAction(user_id, 'typing')
        telebot.sendMessage(user_id, jokesTexts[joke])
        print(user_id)

MessageLoop(telebot, handle).run_as_thread()
while (1):
    subreddit = reddit.subreddit('Jokes')
    hot_python = subreddit.hot(limit=LIMIT)
    jokesTitles = []
    jokesTexts = []
    for submission in hot_python:
        if not submission.stickied:
            jokesTitles.append(submission.title)
            jokesTexts.append(submission.selftext)
    print('Updated list! {} {}'.format(len(jokesTitles), len(jokesTexts)))
    time.sleep(3600)
