import praw
from config import bot_username, bot_password

r = praw.Reddit(user_agent='Mind The Gap Bot')

r.login(bot_username, bot_password)

submissions = r.get_subreddit('test').get_hot(limit=5)

reply_text='Mind that gap '

for submission in submissions:
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        if "Spurs" in comment.body:
            comment.reply(reply_text)
