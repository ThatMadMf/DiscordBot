import random

import requests
from discord.ext import commands


class TextChannel(commands.cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='ping')
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.Cog.listener(name='flip')
    async def flip(self, ctx):
        coin = ['heads', 'tails']
        response = f'You got {random.choice(coin)}, sir'
        await ctx.send(response)

    @commands.Cog.listener(name='dice')
    async def dice(self, ctx):
        response = f'You got {random.randint(1, 6)} , sir'
        await ctx.send(response)

    @commands.Cog.listener(name='image')
    async def image(self, ctx):
        try:
            img_urls = ['https://imgur.com/random']
            pp = requests.get(url=random.choice(img_urls))
            response = pp.url
            await ctx.send(response)
        except Exception:
            print(Exception)
