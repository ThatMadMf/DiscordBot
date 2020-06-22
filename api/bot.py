import os
import random

import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    back_responses = [
        'no fuck u',
        'uno reverse',
        'yeah, whatever'
    ]

    if message.content == 'bot, fuck u':
        response = random.choice(back_responses)
        await message.channel.send(response)

    if message.content == 'bot, roll dice':
        response = f'You got {random.randint(0, 6)} , sir'
        await message.channel.send(response)

    if message.content == 'bot, random number':
        response = f'Random(0-100): {random.randint(0, 100)}'
        await message.channel.send(response)

    if message.content == 'bot, flip a coin' or message.content == '/flip':
        coin = ['heads', 'tails']
        response = f'You got {random.choice(coin)}, sir'
        await message.channel.send(response)

    if message.content == 'bot, send image':
        try:
            img_urls = ['https://imgur.com/random']
            pp = requests.get(url=random.choice(img_urls))
            response = pp.url
            await message.channel.send(response)
        except Exception:
            print(Exception)
            
    if message.content == 'Ceb!':
        amount = random.randint(0, 10)
        if amount == 10:
            await message.channel.send('Ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeb!')
        if amount > 7 < 10:
            await message.channel.send('Ceeeeeeeeeeeeeeeeeeeeeeeb!')
        else:
            await message.channel.send('Ceeeeeeeeb!')

client.run(TOKEN)

