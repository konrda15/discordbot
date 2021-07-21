import discord

async def ex(args, message):
    output = ' '.join(args)
    await message.channel.send(output)
