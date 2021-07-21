import random
import datetime
from datetime import datetime
from datetime import timedelta


async def ex(args, message):
    output = ' '.join(args[0:-1])

    if ';' in output:
        await message.channel.send("not allowed to use ; in remind")
        return

    if len(args) <= 1:
        await message.channel.send("correct usage: ~remind message [number of minutes]")
        return

    file1 = open("commands/data/remind.txt", "a")

    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    lastarg = args[-1]
    n = 0
    try:
        n = int(lastarg)
    except ValueError:
        await message.channel.send("Invalid input")
        return

    if n < 1 or n > 1440:
        await message.channel.send("Number of minutes must be between 1 and 1440")
        return


    remindertime = now + timedelta(minutes=n)

    file1.write(remindertime.strftime("%d/%m/%Y %H:%M:%S") + ";" + message.author.mention + ";" + output + ";" + str(message.guild.id) + ";" + str(message.channel.id) + "\n")

    await message.channel.send("reminder \"" + output + "\" was set for " + remindertime.strftime("%d/%m/%Y %H:%M"))


async def checkremind(client):
    file1 = open("commands/data/remind.txt", "r")

    lines = file1.readlines()
    file1.close()

    file2 = open("commands/data/remind.txt", "w")

    found = False

    for line in lines:
        line_time = datetime.strptime(line.split(';')[0], "%d/%m/%Y %H:%M:%S")
        if line_time < datetime.now():
            guild = int(line.split(';')[3])
            channel = int(line.split(';')[4])
            await client.get_guild(guild).get_channel(channel).send("**reminder: **" + line.split(';')[1] + " " + line.split(';')[2].strip('\n'))
        else:
            file2.write(line)

    file2.close()