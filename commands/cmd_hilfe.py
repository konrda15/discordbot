import discord


async def ex(args, message):
    output = "**~hilfe** - Liste aller Befehle\n" + \
             "**~sag [x]** - postet x\n" + \
             "**~choice [x1, x2 ... xn]<** - wählt eine der n Optionen\n" + \
             "**~janein** - antwortet mit ja, nein oder vielleicht\n" + \
             "**~rand [x, y]** - zufällige Zahl zwischen x und y\n" + \
             "**~rate [x]** - bewertet x auf einer Skala zwischen 0 und 10\n" + \
             "**~react** - postet ein zufälliges emote als Reaktion\n" + \
             "**~remind [x, n]** - erinnert den User nach n Minuten\n" + \
             "**~remremind [x]** - entfernt Erinnerung x\n" + \
             "**~tipp [x]** - postet Tipp für Spiel x\n" + \
             "**~warn [user]** - verwarnt user\n"

    embed = discord.Embed(description=output)
    await message.channel.send(embed=embed)