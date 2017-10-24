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


@client.event
async def on_ready(): #when the discord api has logged in and is ready then this even is fired
    print("ready")
    for server in client.servers: #this sifts through all the bots servers and gets the channel we want
            #should probly add a check in for the server in here im guessing
            for channel in server.channels:
                if channel.name == "serverchat" and str(channel.type) == "text": #checks if the channel name is what we want and that its a text channel
                    channelToUse = channel #saves the channel that we wanna use since we found it    
    counter = 0
    for server in client.servers: #this sifts through all the bots servers and gets the channel we want
            #should probly add a check in for the server in here im guessing
            for channel in server.channels:
                data = []
                print(str(channel.name))
                if "" == "":
                    async for message in client.logs_from(channel, limit=999999999):
                        counter = counter + 1
                        ts = message.timestamp
                        d = datetime.timedelta(days=1)
                        print(message.timestamp)
                        t = ts - d
                        #print(message.clean_content)
                        #print(message.attachments)
                        msg = {"time":str("{:%Y-%m-%d %H:%M}".format(message.timestamp)), "author": str(message.author.name), "message": str(message.clean_content), "server": str(message.server.name), "channel": str(message.channel.name),"attachments": list(message.attachments)}
                        data.append(msg)
                        print(str("{:%Y-%m-%d %H:%M}".format(message.timestamp)) + ":" + "[{1}-{0}]".format(message.channel.name,message.server.name)+ str(message.author.name) + ":" + str(message.clean_content))
                    print(counter)
                    name = str(server.name)+ "-" + str(channel.name) + ".txt"
                    fileSave(name,data)
    print(str("{:%y:%m:%d:%H:%M}".format(message.timestamp)) + ":" + str(message.author) + ":" + str(message.content),)
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
