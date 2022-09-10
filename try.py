import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in asd {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("asd"):
        await message.channel.send("dsa")

client.run(os.getenv("TOKEN"))