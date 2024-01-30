import os

import slackelient

slack_token = os.getenv("SLACK_TOKEN")
client = SlackClient(slack_token)

def channel_list(client):
    channels = client.api_call("channels.list")
    if channels['ok']:
        return channels['channels']
    else:
        return None
