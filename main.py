import json

import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

keep_alive()

with open("config.json") as f:
    config = json.load(f)

try:
    token = os.environ["TOKEN"]
except KeyError:
    token = config["TOKEN"]

try:
    prefix = config["PREFIX"] or "m!"
except KeyError:
    prefix = "m!"


intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), case_insensitive = True, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="músicas"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Carregado: {filename}")

client.run(token)