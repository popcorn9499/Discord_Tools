import datetime
#used for the main program
import threading

import json

import sys, os
#discord stuff imported
import discord #gets the discord and asyncio librarys
import asyncio
import time
data = []
client = discord.Client()

def fileSave(fileName,config):
    print("Saving")
    f = open(fileName, 'w') #opens the file your saving to with write permissions
    f.write(json.dumps(config,sort_keys=True, indent=4 ) + "\n") #writes the string to a file
    f.close() #closes the file io

def fileLoad(fileName):#loads files
    with open(fileName, 'r') as handle:#loads the json file
        config = json.load(handle) 
    return config    

@client.event
async def on_ready(): #when the discord api has logged in and is ready then this even is fired
    discordInfo = {}
    for server in client.servers: #this portion gets all the info for all the channels and servers the bot is in
        discordInfo.update({str(server): {"asdasdhskajhdkjashdlk":"channel info"}})#maybe set a check for that channel
        for channel in server.channels:
            disc = {str(channel.name): channel}
            discordInfo[str(server)].update(disc)
    data = fileLoad("Popicraft Streams-popcorn9499s-stream-chat.txt")
    for i in range(len(data)-1,-1,-1):
        dataX = data[i]
        print( dataX["time"] + " - " + "[{1}-{0}] ".format(dataX["channel"],dataX["server"])+ dataX["author"] + ": " + dataX["message"])
        if len(data[i]["attachments"]) == 0:
            await client.send_message(discordInfo["Popicraft Network"]["stream-chat"], dataX["time"] + " - " + "[{1}-{0}] ".format(dataX["channel"],dataX["server"])+ dataX["author"] + ": " + dataX["message"]) #sends the message to the channel specified in the beginning
        else:
            attachmentURLS = ""
            for i in dataX["attachments"]:
                attachmentURLS = i['url']
            await client.send_message(discordInfo["Popicraft Network"]["stream-chat"], dataX["time"] + " - " + "[{1}-{0}] ".format(dataX["channel"],dataX["server"])+ dataX["author"] + ": " + dataX["message"] + " {0}".format(attachmentURLS)) #sends the message to the channel specified in the beginning

                
    #fileSave(name,data)
    print(str("{:%y:%m:%d:%H:%M}".format(message.timestamp)) + ":" + str(message.author) + ":" + str(message.content))
    print("next")
    # while message.content != "":
        # async for message in client.logs_from(channelToUse, limit=500, before=ts, after=t):
            # ts = message.timestamp
            # d = datetime.timedelta(days=1)
            # t = ts - d
            # print(str("{:%y:%m:%d:%H:%M}".format(message.timestamp)) + ":" + str(message.author) + ":" + str(message.content),)
        # print("waiting")
       
    # print(str("{:%y:%m:%d:%H:%M}".format(message.timestamp)) + ":" + str(message.author) + ":" + str(message.content),)
    
# @client.event
# async def on_message(message): #waits for the discord message event and pulls it somewhere    
    # ts = message.timestamp
    # d = datetime.timedelta(days=1)
    # t = ts - d
    # messages = yield from  client.logs_from("test", limit=5000, before=ts, after=t) #after fetching, contains every message 50 times
    # # print(messages.author)
    # for m in messages:
        # print(m)


client.run("Token")