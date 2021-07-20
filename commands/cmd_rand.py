import random


async def ex(args, message):
    if len(args) < 2:
        await message.channel.send("Wrong input!")
        return
    start = int(args[0])
    end = int(args[1])

    try:
        result = str(random.randint(start, end))
        await message.channel.send(result)
    except:
        await message.channel.send("Error!")
