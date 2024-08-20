import random


async def ex(args, message):
    result = random.randint(0, 1000)
    output = "Nein"
    if (result % 2 == 0):
        output = "Ja"
    elif (result % 37 == 0):
        output = "Vielleicht"
    elif (result % 41 == 0):
        output = "Ich weiß nicht"
    elif (result % 43 == 0):
        output = "Kannst du die Frage wiederholen?"
    elif (result == 500):
        output = "Des is die nächste depperte Frog!"
    elif (result == 600):
        output = "Ich kenn mich da nicht aus, möchte mich dazu nicht äußern also bitte respektier das."

    await message.channel.send(output)
