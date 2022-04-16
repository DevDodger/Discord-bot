import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") 

@bot.event
async def on_connect():
  print ("Bot has started!")
  await bot.change_presence(status=discord.Status.online,activity=discord.Game('Video Testing!'))

#commands
@bot.command()
async def test(ctx):
  await ctx.send ("Test Back!")

@bot.command()
async def hello(ctx):
  await ctx.send ("How are you!")

@bot.command()
async def github(ctx):
  await ctx.send ("https://github.com/DevDodger/Discord-bot/blob/main/main.py")

#DO NOT TOUCH!

TOKEN = "ur token"

bot.run(TOKEN)
