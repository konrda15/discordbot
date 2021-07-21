import asyncio
from commands import cmd_remind


async def updateloop(client):
    while True:
        await cmd_remind.checkremind(client)
        await asyncio.sleep(20)
