import random
from commands import cmd_react

async def eventselector(message):
    r = random.randint(0, 1000)
    if r < 10:
        await cmd_react.ex("", message)


