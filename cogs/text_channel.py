import asyncio
import json
import os
import random

import requests
from googletrans import Translator
from discord.ext import commands

IMAGE_SECRET = os.environ.get('KSOFT_SECRET')


class TextChannel(commands.Cog):
    def __init__(self, bot):
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

    @commands.command(name='image', aliases=['i'])
    async def image(self, ctx):
        await ctx.message.delete()
        img_urls = ['https://api.ksoft.si/images/random-meme', 'https://api.ksoft.si/images/rand-reddit/dankmemes']
        pp = requests.get(url=random.choice(img_urls), headers={'Authorization': f'Bearer {IMAGE_SECRET}'})
        url = json.loads(pp.text).get('image_url')
        response = await ctx.send(url)
        await asyncio.sleep(60)
        await response.delete()

    @commands.command(name='translate',  aliases=['t', 'tr'],
                      description='Translates text in format [lang] [text] e.g: ru "text to translate"')
    async def translate(self, ctx, *args):
        if not 1 <= len(args) <= 2:
            print('Bad request')
            return

        if len(args) == 1:
            target = 'en'
            text = args[0]
        else:
            target = args[0]
            text = args[1]

        translator = Translator()
        try:
            translated_text = translator.translate(text, dest=target)
        except ValueError:
            await ctx.send(f'You probably screwed up with destination language. Look it up. Or maybe try use quotes')
            return

        await ctx.send(f'original: {text} \ntranslated: {translated_text.text}\n')


def setup(bot):
    bot.add_cog(TextChannel(bot))
