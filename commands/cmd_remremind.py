import random
import datetime
from datetime import datetime
from datetime import timedelta


async def ex(args, message):
    delete = ' '.join(args)

    file1 = open("commands/data/remind.txt", "r")

    lines = file1.readlines()
    file1.close()

    file2 = open("commands/data/remind.txt", "w")

    found = False

    for line in lines:
        if line.split(';')[2].strip('\n') != delete:
            file2.write(line)
        else:
            found = True
    file2.close()

    if found:
        await message.channel.send(delete + " was deleted")
    else:
        await message.channel.send(delete + " was not found")