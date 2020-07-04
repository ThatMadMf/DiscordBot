import asyncio
import os
import random

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='/')

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')


@bot.command(name='join')
async def join_voice(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()


@bot.command(name='leave')
async def leave_voice(ctx):
    try:
        for x in bot.voice_clients:
            return await x.disconnect()
    except Exception:
        return ctx.send('WTF')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name='flip')
async def flip(ctx):
    coin = ['heads', 'tails']
    response = f'You got {random.choice(coin)}, sir'
    await ctx.send(response)


@bot.command(name='dice')
async def dice(ctx):
    response = f'You got {random.randint(1, 6)} , sir'
    await ctx.send(response)


@bot.command(name='image')
async def image(ctx):
    try:
        img_urls = ['https://imgur.com/random']
        pp = requests.get(url=random.choice(img_urls))
        response = pp.url
        await ctx.send(response)
    except Exception:
        print(Exception)


@bot.command(name='play', pass_context=True)
async def play(ctx):
    guild = ctx.guild
    voice_client = discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    voice_client.play(discord.FFmpegPCMAudio('shatt.mp3'))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 10.0
    while voice_client.is_playing():
        await asyncio.sleep(1)
    voice_client.stop()

bot.run(AUTH_TOKEN)
