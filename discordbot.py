
import discord
import random
from discord.ext import commands


TOKEN = ''
GUILD = 'MetroPlex'

bot = commands.Bot(command_prefix='!')
    
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ping', help='Yes')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'minecraft' in message.content:
        await message.channel.send('minecraft is pretty cool.')



bot.run(TOKEN)