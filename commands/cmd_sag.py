import discord

async def ex(args, message):
    output = ""
    for arg in args:
        output += arg
        output += " "
    await message.channel.send(output)
