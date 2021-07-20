from discord import Embed, Color
from datetime import datetime


async def ex(args, message):
    if len(args) == 0:
        await message.channel.send("Wrong input!")
        return

    server = message.guild

    warnedUser = ""
    warnedUserNick = ""

    if len(message.mentions) == 0:
        await message.channel.send("User not found!")
        return

    warnedUser += message.mentions[0].mention
    warnedUserNick += message.mentions[0].name

    reason = ""
    for s in args:
        if s == args[0]:
            continue
        reason += s
        reason += " "

    if reason == "":
        reason = "-"

    mod = ""
    mod += message.author.mention

    output = "**" + warnedUser + " has been warned!**"
    await message.channel.send(output)

    logTitle = "**Warn | " + warnedUserNick + "**"

    embed = Embed(color=Color.red(), title=logTitle)
    embed.add_field(name="User", value=warnedUser, inline=True)
    embed.add_field(name="Moderator", value=mod, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    dateTimeObj = datetime.now()
    embed.set_footer(text=(dateTimeObj.strftime("%d.%m.%Y, %H:%M:%S")))

    for channel in server.channels:
        if channel.name == "mod-logs": #hardcoded value
            await channel.send(embed=embed)

