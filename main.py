from cmdlist import cmd
from secretcmdlist import secretcmd
import asyncio
import SECRETS
import discord
from discord import Game, Embed, Color

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('~'):
        invoke = message.content[len('~'):].split(" ")[0]
        args = message.content.split(" ")[1:]

        if invoke in cmd:
            await cmd[invoke].ex(args, message)
        elif invoke in secretcmd:
            await secretcmd[invoke].ex(args, message)
        else:
            await message.channel.send(embed=Embed(color=Color.red(), description="not valid"))


client.run(SECRETS.TOKEN)
