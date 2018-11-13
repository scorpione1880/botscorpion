import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='stuck in scorpions house'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$ping':
        await client.send_message(message.channel,'pong!')
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('niggers') in message.content:
       await client.delete_message(message)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if message.content == '$fuck':
        await client.send_message(message.channel,'me')
    if message.content.startswith('$rannum'):
        randomlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('$cointoss'):
        randomlist = ["heads", "tails",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('$truefalse'):
        randomlist = ["true", "false",]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTExNjc5MDMxMTIxMjgxMDI0.Dsui9A.oPK-fX-ugRNbybg8di9IjMKufiY')
