import random

import requests
from discord.ext import commands


class TextChannel(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command(name='flip')
    async def flip(self, ctx):
        coin = ['heads', 'tails']
        response = f'You got {random.choice(coin)}, sir'
        await ctx.send(response)

    @commands.command(name='dice')
    async def dice(self, ctx):
        response = f'You got {random.randint(1, 6)} , sir'
        await ctx.send(response)

    @commands.command(name='image')
    async def image(self, ctx):
        try:
            img_urls = ['https://imgur.com/random']
            pp = requests.get(url=random.choice(img_urls))
            response = pp.url
            await ctx.send(response)
        except Exception:
            print(Exception)


def setup(bot):
    bot.add_cog(TextChannel(bot))
