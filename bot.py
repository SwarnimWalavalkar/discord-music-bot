import os
import discord
from discord.ext import commands
from .src.Music import Music

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
Music.setup(client)

client.run(os.getenv("BOT_TOKEN"))