import os
from slackclient import SlackClient


# CPS-847-Bot Slack
Bot_User_OAuth_Access_Token = 'Add User Authentication Token'
SLACK_API_TOKEN = Bot_User_OAuth_Access_Token

# Hardcoded SLACK_API_TOKEN
slack_token = SLACK_API_TOKEN
client = SlackClient(slack_token)

def say_hello(data):
    #print(data)
    try:
        #if 'Hello' in data['text']:
            dataMessage = data['text'] #this allows the message to be stored into a 
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user'] #user id

            client.api_call('chat.postMessage',
                channel=channel_id, #channel id is the communication id between the bot 
                text=""+dataMessage, 
                thread_ts=thread_ts
        )
    except: 
        print("")

if client.rtm_connect(): #this connects to the slack api using real time messsaging 
    while client.server.connected is True:
        for data in client.rtm_read(): #while you have something inputed, the json file will be created and the client will read it 
            if "type" in data and data["type"] == "message": #This is checking the json file for a type field and making sure that type field contains a message
                say_hello(data) #data is a whole json file that is being inserted into the function to extract certain values
else:
    print("Connection Failed")

