import random


async def ex(args, message):
    result = random.randint(0, 1000)
    output = "Nein"
    if (result % 2 == 0):
        output = "Ja"
    if (result <= 30):
        output = "Vielleicht"

    await message.channel.send(output)
