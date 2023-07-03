import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def hallo(ctx):
  await ctx.send('Hallo, wie geht es dir. Ich bin der neue Bot auf diesem Server!')

bot.run('')
