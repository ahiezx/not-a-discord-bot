import discord, auth, config
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
	print("Made by {}\n{} {}".format(config.AUTHOR,client.user.name, config.VERSION))

client.run(auth.TOKEN)
