import random


async def ex(args, message):
    output = ' '.join(args)

    rating = random.randint(0, 10)
    output += " **[" + str(rating) + "/10]**"

    await message.channel.send(output)
