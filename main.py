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

    if (message.content.lower() == 'bom dia'):
        await message.add_reaction("<:riosball:587061815788437509>")
        response = 'Bom dia pra quem porra <:riosball:587061815788437509>'
        await message.add_reaction("<:riosball:587061815788437509>")

        await message.channel.send(response)

    if (message.content.lower() == 'boa tarde'):
        await message.add_reaction("<:riosball:587061815788437509>")
        response = 'Boa tarde pra quem porra <:riosball:587061815788437509>'
        await message.add_reaction("<:riosball:587061815788437509>")

        await message.channel.send(response)

    if (message.content.lower() == 'boa noite'):
        await message.add_reaction("<:riosball:587061815788437509>")
        response = 'Boa noite pra quem porra <:riosball:587061815788437509>'
        await message.add_reaction("<:riosball:587061815788437509>")

        await message.channel.send(response)
    if (message.content.lower() == 'boa madrugada'):
        await message.add_reaction("<:riosball:587061815788437509>")
        response = 'Boa madrugada pra quem porra <:riosball:587061815788437509>'
        await message.add_reaction("<:riosball:587061815788437509>")

        await message.channel.send(response)

keep_alive.keep_alive()
client.run(token)

