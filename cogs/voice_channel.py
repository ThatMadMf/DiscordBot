import asyncio

import discord
from discord.ext import commands


class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    async def join_voice(self, ctx):
        connected = ctx.author.voice
        if connected:
            await ctx.message.delete()
            await connected.channel.connect()

    @commands.command(name='leave', pass_context=True)
    async def leave_voice(self, ctx):
        guild = ctx.guild
        voice_client = discord.utils.get(self.bot.voice_clients, guild=guild)
        await ctx.message.delete()
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


def setup(bot):
    bot.add_cog(VoiceChannel(bot))
