import discord
from discord.ext import commands
from discord import app_commands
from mainconf import *
from database import *
from bandb.py import *
from logdb import *


@bot.tree.command(name="prioone", description="Prio 1 Command")
@app_commands.guilds(discord.Object(id=main))
async def leave(interaction: discord.Interaction):
  devs = await getdevs()
  ops = await getops()
  service = await serviceowner()
  if str(interaction.user.id) in devs or ops or service:
    await interaction.response.send_message('Prio 1 Command')
  else:
    print('Handling of not authorized not required if not deleting response and ephemeral is not true')

@bot.tree.command(name="priotwo", description="Prio 2 Command")
@app_commands.guilds(discord.Object(id=main), *[discord.Object(id=guild_id) for guild_id in subserver])
async def listdevs(interaction: discord.Interaction):
  devs = await getdevs()
  ops = await getops()
  service = await serviceowner()
  if str(interaction.user.id) in devs or ops or service:
    await interaction.response.send_message('Prio 2 Command') 

@bot.tree.command(name="priothree", description="Prio 3 Command")
@app_commands.guilds(discord.Object(id=main), *[discord.Object(id=guild_id) for guild_id in subserver], *[discord.Object(id=guild_id) for guild_id in miscservers]))
async def listdevs(interaction: discord.Interaction):
  devs = await getdevs()
  ops = await getops()
  service = await serviceowner()
  if str(interaction.user.id) in devs or ops or service:
    await interaction.response.send_message('Prio 3 Command')

await bot.run('token')
