# reddit-slackbot

This is a script that will watch new posts to a subreddit and if it finds a new submission then it will send the link to the submission to the slack channel.

A few things you will need to change in the script.

Get a Slack token for your team and input it here:

`token = "SLACK_API_TOKEN"`

Give your redditbot a user agent:

`user_agent = ("ENTER_USER_AGENT_NAME")`

Enter the name of the subreddit you want to watch new posts for:

`subreddit = r.get_subreddit("ENTER_SUBREDDIT_NAME")`

Finally enter a name for bot Slack channel you want to send the message to:

`sc.api_call("chat.postMessage", username="ENTER_BOT_NAME", channel="ENTER_SLACK_CHANNEL", text=submission.permalink, unfurl_links="true")`

