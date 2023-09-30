import discord
from discord.ext import commands

TOKEN = 'MTE1MzY1NDk2MjQ5NzI2OTgxMQ.GNnPjK.iRQYCcaQGywe-wxOIcW9NAnocJdEfFn58lCC2k'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online.')

@bot.command()
async def hello(ctx):
    await ctx.send('Hey There!, Howdy!!')

@bot.command()
async def help1(ctx):
    await ctx.send('!livescore: Gives live cricket scores!\n!help1: All commands I can do :)\n!hello: I can say hello too!!\n!generate: All data you fetched about cricket events!!')

bot.run(TOKEN)
