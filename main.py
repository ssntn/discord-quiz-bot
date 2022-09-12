import discord
import win_commands
import os

# question = commands.random_command()
# print("\n\nQuestion",question,"\n")
# print("Choice: ", commands.choices(question[1]))

print(win_commands)
print("\n\n")
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("We have logged in asd {0.user}".format(client))


@client.event
async def on_message(message):
	
	if message.author == client.user:
		return

	if message.content.startswith("asd"):
		await message.channel.send("dsa")


token = os.environ["token"]
client.run(token)
print(token)
