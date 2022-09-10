import discord
import commands

question = commands.random_command()
print("\n\nQuestion",question,"\n")
print("Choice: ", commands.choices(question[1]))