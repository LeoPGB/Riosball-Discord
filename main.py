import os

import discord
import asyncio
import keep_alive
import random as r
import linecache as lc
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content == 'bom dia' or message.content == 'Bom dia'):
        response = 'Bom dia pra quem porra'

        await message.channel.send(response)

    if (message.content == 'boa tarde' or message.content == 'Boa tarde'):
        response = 'Boa tarde pra quem porra'

        await message.channel.send(response)

    if (message.content == 'boa noite' or message.content == 'Boa noite'):
        response = 'Boa noite pra quem porra'

        await message.channel.send(response)
    if (message.content == 'boa madrugada' or message.content == 'Boa madrugada'):
        response = 'Boa madrugada pra quem porra'

        await message.channel.send(response)

keep_alive.keep_alive()
client.run(token)
