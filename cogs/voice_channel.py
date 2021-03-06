import asyncio
import os
import random

import discord
import youtube_dl as youtube_dl
from discord.ext import commands
from gtts import gTTS


class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.volume = 0.5

    @commands.command(name='join')
    async def join_voice(self, ctx):
        greetings = ['hi guys', 'hello', 'whats popping', 'whats up']
        connected = ctx.author.voice
        if connected:
            await ctx.message.delete()
            await connected.channel.connect()
            await ctx.invoke(self.bot.get_command('say'), random.choice(greetings))

    @commands.command(name='leave', pass_context=True)
    async def leave_voice(self, ctx):
        farewells = ['good by', 'farewell', 'see you']
        guild = ctx.guild
        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        await ctx.message.delete()
        await ctx.invoke(self.bot.get_command('say'), random.choice(farewells))
        await voice_client.disconnect()

    @commands.command(name='say', pass_context=True)
    async def say(self, ctx, text):
        tts = gTTS(text)
        with open('reserved_files/message.mp3', 'wb') as f:
            tts.write_to_fp(f)
        try:
            await ctx.message.delete()
        except discord.NotFound:
            print('Nothing to delete')
        guild = ctx.guild

        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        voice_client.play(discord.FFmpegPCMAudio('reserved_files/message.mp3'))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = self.volume
        while voice_client.is_playing():
            await asyncio.sleep(1)
        voice_client.stop()

    @commands.command(name='play', aliases=['p'], pass_context=True)
    async def play(self, ctx, url):

        await ctx.message.delete()

        url = url.split('&')[0]

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': 'temp.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            audio = ydl.extract_info(url=url, download=True)

        guild = ctx.guild

        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        voice_client.play(discord.FFmpegPCMAudio('temp.mp3'))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = self.volume
        while voice_client.is_playing():
            await asyncio.sleep(1)
        voice_client.stop()

    @commands.command(name='volume', pass_context=True)
    @commands.has_permissions(administrator=True)
    async def volume(self, ctx, volume):
        await ctx.message.delete()
        try:
            volume = int(volume)
        except ValueError:
            return

        if not 0 < volume <= 100:
            return
        self.volume = volume / 100
        response = await ctx.send(f'Volume set to {volume}')
        await asyncio.sleep(10)
        await response.delete()


def setup(bot):
    bot.add_cog(VoiceChannel(bot))
