import discord
from discord.ext import commands
import os
import server

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="f!")

@bot.event
async def on_ready():
  print(f"{bot.user.name} has been connected")

@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! in `{round(bot.latency * 1000)}`")

bot.load_extension('jishaku')
server.server()
bot.run(TOKEN)
