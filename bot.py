import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
client = discord.Client()
#prefix
client = commands.Bot(client,commmand_prefix = "yee")
#image
yee = discord.Embed()
yee.set_image(url="https://pbs.twimg.com/profile_images/504715443479670784/fauyuPDy_400x400.png")
#online
@client.event
async def on_ready():
    print("Ready")
    print("I am " + client.user.name)
    print("ID: " + client.user.id)
@client.event
async def on_message(message):
    userID = message.author.id
    if message.content.startswith("ye"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Alexa this is so sad can we play despacito" % (userID))
        await client.send_message(message.channel, "https://pbs.twimg.com/profile_images/504715443479670784/fauyuPDy_400x400.png")
    




client.run(os.getenv('TOKEN'))
