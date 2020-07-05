import asyncio
import random

import discord
from discord.ext import commands
from gtts import gTTS


class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(name='play', pass_context=True)
    async def play(self, ctx):
        await ctx.message.delete()
        guild = ctx.guild

        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        voice_client.play(discord.FFmpegPCMAudio('shatt.mp3'))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 10.0
        while voice_client.is_playing():
            await asyncio.sleep(1)
        voice_client.stop()

    @commands.command(name='say', pass_context=True)
    async def say(self, ctx, text):
        tts = gTTS(text)
        with open('message.mp3', 'wb') as f:
            tts.write_to_fp(f)
        try:
            await ctx.message.delete()
        except discord.NotFound:
            print('Nothing to delete')
        guild = ctx.guild

        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        voice_client.play(discord.FFmpegPCMAudio('message.mp3'))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 10.0
        while voice_client.is_playing():
            await asyncio.sleep(1)
        voice_client.stop()


def setup(bot):
    bot.add_cog(VoiceChannel(bot))
