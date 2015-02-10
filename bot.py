import praw
from config import bot_username, bot_password
r = praw.Reddit(user_agent='Mind The Gap Bot')
r.login('bot_username', 'bot_password')
submissions = r.get_subreddit('soccer').get_hot(limit=5)
for x in submissions:
	print str(x)