import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='/')

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

cogs = [
    'cogs.text_channel',
    'cogs.voice_channel'
]

for cog in cogs:
    bot.load_extension(cog)

bot.run(AUTH_TOKEN)
