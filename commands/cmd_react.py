import random


async def ex(args, message):
    emojis = await message.guild.fetch_emojis()
    index = random.randint(0, len(emojis) - 1)

    await message.add_reaction(emojis[index])

    if random.randint(0, 9) == 0:
        await ex(args, message)
