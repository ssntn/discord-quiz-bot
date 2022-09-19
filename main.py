import discord
import os
import win_commands as wc
import numpy as np


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in asd {0.user}".format(client))

# \U0000030
@client.event
async def on_message(message):
	# DO NOT CROSS THIS LINE # DO NOT CROSS THIS LINE # DO NOT CROSS THIS LINE
	if message.author == client.user:
		return

	# DO NOT CROSS THIS LINE # DO NOT CROSS THIS LINE # DO NOT CROSS THIS LINE

	if message.content.startswith('$hello'):
		await message.channel.send(
			'Hello I am Quizzerino with a greeterino! Let\'s see your skills, type $quiz')

	if message.content.startswith("$quiz"):
		BUTTON_MODE = 0
		NAME_MODE = 1

		quiz = wc.quiz(BUTTON_MODE)
		question = quiz["question"]
		choices = quiz["choices"]
		answer = quiz["answer"]

		choice_str = ""
		print(choices.size)
		for i in range(choices.size):
			choice_str = choice_str+ str(i+1) +": "+choices[i]+"\n"

		msg = await message.channel.send(f"\nWhich command: {question}\n{choice_str}\nAnswer: {answer}")
		
		emojis = ["1️⃣","2️⃣","3️⃣", "4️⃣"]
		for e in emojis:
			await msg.add_reaction(e)


 # DELETE THIS LINE # DELETE THIS LINE # DELETE THIS LINE # DELETE THIS LINE
client.run(os.environ['TOKEN'])