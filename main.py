import discord
import os
import win_commands as wc

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in asd {0.user}".format(client))


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
		rand_ind = wc.random_command()
		mode = 0
		question = None
		answer = None
		
		# BUTTON MODE: predef button, mode=0
		if(mode == 0):
			question = rand_ind[0]
			answer = rand_ind[1]

		# NAME MODE: predef name, mode=1
		elif(mode == 1):
			question = rand_ind[1]
			answer = rand_ind[0]


		choices = wc.choices(answer, mode)
		await message.channel.send(f"What is the buttons for {question}\n{choices}")

 # DELETE THIS LINE # DELETE THIS LINE # DELETE THIS LINE # DELETE THIS LINE

client.run(os.environ['TOKEN'])