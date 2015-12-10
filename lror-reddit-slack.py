#!/usr/bin/python
import praw
import os
from slackclient import SlackClient

# Connection to slack
token = "SLACK_API_TOKEN"
sc = SlackClient(token)

# Create user agent for Reddit api
user_agent = ("LearnRoR-Slack Bot 0.1")

# Create connection to reddit
r = praw.Reddit(user_agent = user_agent)

# Storing id's of submissions in a text file for now. That should eventually 
# be stored in a database, probably sqlite

# First check to see if the file exists, if it doesn't create empty array to
# store the submission ids
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

# If the file does exist then read it in, split on the new line characters
# and filter out None as it's possible to have a blank file
else:
	with open ("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = filter(None, posts_replied_to)

# Praw call to connect to our subreddit of choice!
subreddit = r.get_subreddit("ENTER_SUBREDDIT_NAME")

# Loop through the new submissions. We're only grabbing 5 each time
for submission in subreddit.get_new(limit=5):
	#Does our submission already exist?
	if submission.id not in posts_replied_to:
		# If not, let's make our call to slack to post the submission and store
		#the submission.id in our array of posts we've replied to
		sc.api_call("chat.postMessage", username="new post bot", channel="ENTER_SLACK_CHANNEL", text=submission.permalink, unfurl_links="true")
		posts_replied_to.append(submission.id)

# Open our text file and write out the new submission.id so we don't 
# post it again.
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
