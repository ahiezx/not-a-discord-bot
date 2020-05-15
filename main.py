import discord, auth, config
from database.main import *
from time import sleep

bot = discord.Client()
bot.db = MySQL(auth.HOST, auth.USER, auth.PASS, auth.PORT)
@bot.event
async def on_ready():
	print("Made by {}\n{} {}".format(config.AUTHOR,bot.user.name, config.VERSION))

bot.run(auth.TOKEN)
