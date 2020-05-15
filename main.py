import discord, auth
from time import sleep
client = discord.Client()

@client.event
async def on_ready():
	for x in client.users:
		print(x.name)

client.run(auth.TOKEN)
