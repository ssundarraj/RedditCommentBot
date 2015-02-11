import praw
from config import bot_username, bot_password

r = praw.Reddit(user_agent='Mind The Gap Bot')

r.login(bot_username, bot_password)
print "Logged in"

submissions = r.get_subreddit('soccer').get_hot(limit=100)
print "Got posts"

reply_text='Mind that gap http://i.imgur.com/8uEKnyu.png'

for submission in submissions:
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        try:
            if "Spurs" in comment.body:
                print comment.body
                comment.reply(reply_text)
        except:
            pass