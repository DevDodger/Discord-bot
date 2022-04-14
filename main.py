import discord
from discord.ext import commands
from webserver import keep_alive
import os
import time

bot = commands.Bot(command_prefix="!") 

@bot.event
async def on_connect():
  print ("GUSD bot has started!")
  await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game('Your Bot!'))
  
#commands
@bot.command()
async def test(ctx):
  await ctx2.send ("Test Back!")




keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
