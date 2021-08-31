import os
import discord
from discord.ext import commands
import music

from dotenv import load_dotenv
load_dotenv()

cogs = [music]

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run(os.getenv("BOT_TOKEN"))