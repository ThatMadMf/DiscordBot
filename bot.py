import os

from discord.ext import commands
from dotenv import load_dotenv

from cogs.text_channel import TextChannel
from cogs.voice_channel import VoiceChannel

load_dotenv()

bot = commands.Bot(command_prefix='/')

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

bot.add_cog(TextChannel(bot))
bot.add_cog(VoiceChannel(bot))

bot.run(AUTH_TOKEN)
