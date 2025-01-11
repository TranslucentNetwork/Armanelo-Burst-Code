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

@bot.tree.command(name="priotwo", description="Prio 2 Command")
@app_commands.guilds(discord.Object(id=main), *[discord.Object(id=guild_id) for guild_id in subserver],*[discord.Object(id=guild_id) for guild_id in miscservers]))
async def listdevs(interaction: discord.Interaction):
  devs = await getdevs()
  ops = await getops()
  service = await serviceowner()
  if str(interaction.user.id) in devs or ops or service:
    await interaction.response.send_message('Prio 3 Command')

await bot.run('token')


#How to Contribute
#As a contributor, your responsibility is to create the commands based on the specified functionality and submit them via a pull request.

#I will handle all the necessary configuration, including:

#Assigning the correct priority and access levels for each command.
#Setting up the appropriate server-specific permissions and roles.
#Integrating commands with the database to ensure they function as expected.
#Simply ensure that the command is defined, and include any relevant parameters or functionality you want the command to have. Once you've done that, submit it as a pull request, and I will handle the rest.


