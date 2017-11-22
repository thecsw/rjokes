# Fill your Reddit and Telegram API in example.config.py and rename it to config.py
import config
# Telegram library for telegram bot
import telepot
# Library to get new message
from telepot.loop import MessageLoop
# Library to interact with Reddit's API
import praw
# Get random jokes
import random
import time
# Limit of jokes
LIMIT = 100
counter = 0
sub = 'Jokes'
jokesTitles = []
jokesTexts = []
for i in range(0, LIMIT):
    jokesTitles.append('Nothing here... Only pure emptiness')
    jokesTexts.append('Only virtual particles are popping up')
reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

telebot = telepot.Bot(config.token)

def handle(msg):
    global counter
    user_id = msg['chat']['id']
    command = msg['text'].encode('utf-8').lower()
    
    if command == '/joke' or command == '/joke@rjokes_bot':
        joke = random.randint(1, LIMIT-1)
        telebot.sendChatAction(user_id, 'typing')
        time.sleep(1)
        telebot.sendMessage(user_id, jokesTitles[joke])
        telebot.sendChatAction(user_id, 'typing')
        time.sleep(2)
        telebot.sendMessage(user_id, jokesTexts[joke])
        print(user_id)
        print(jokesTitles[joke])
        print(jokesTexts[joke])
        print('\n')
        counter+=1
        print(counter)

    if command == '/help' or command == '/help@rjokes_bot':
        telebot.sendChatAction(user_id, 'typing')
        telebot.sendMessage(user_id, 'Thank you for using the bot that just delivers!\n\
        if you have any questions or suggestions, please dm me on @thecsw')

        
MessageLoop(telebot, handle).run_as_thread()
while (1):
    subreddit = reddit.subreddit(sub)
    #hot_python = subreddit.hot(limit=LIMIT)
    hot_python = subreddit.top('day', limit=LIMIT)
    # Updating jokes by popping at the beginning of the list and adding new one at the end
    # Maybe there is a separate function in python to do this?
    for submission in hot_python:
        if not submission.stickied:
            jokesTitles.pop(0)
            jokesTexts.pop(0)
            jokesTitles.append(submission.title)
            jokesTexts.append(submission.selftext)
    print('Updated list! {} {}'.format(len(jokesTitles), len(jokesTexts)))
    time.sleep(3600)
