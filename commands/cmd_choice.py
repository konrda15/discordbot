from random import randint


async def ex(args, message):
    output = "Error!"

    if len(args) < 1:
        output = "Error!"
    else:
        x = randint(0, len(args)-1)
        output = args[x]

    await message.channel.send(output)
