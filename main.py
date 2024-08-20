from cmdlist import cmd
from secretcmdlist import secretcmd
import asyncio
import SECRETS
import discord
from discord import Game, Embed, Color
from randomevents import eventselector
from regularevents import updateloop

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await eventselector(message)

    if message.content.startswith('~'):
        invoke = message.content[len('~'):].split(" ")[0]
        args = message.content.split(" ")[1:]

        if invoke in cmd:
            await cmd[invoke].ex(args, message)
        elif invoke in secretcmd:
            await secretcmd[invoke].ex(args, message)
        else:
            await message.channel.send(embed=Embed(color=Color.red(), description="not valid"))


@client.event
async def on_ready():
    loop = asyncio.get_event_loop()
    loop.create_task(updateloop(client))

    print("Bot is online. Running on servers:")
    for s in client.guilds:
        print(" - %s (%s)" % (s.name, s.id))
    await client.change_presence(activity=Game(name="[~hilfe]"))


client.run(SECRETS.TOKEN)
