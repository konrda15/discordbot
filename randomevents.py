import random
from commands import cmd_react
from secret_commands import cmd_insult

async def eventselector(message):
    r = random.randint(0, 10000)
    if r < 100:
        await cmd_react.ex("", message)
    elif r < 110:
        await cmd_insult.ex2(message)
    elif r == 500:
        await message.channel.send("Hoit di Goschn du Vuitrottl, du kennst di nix aus du depperter Bua. Geh, tua oabeitn, dann waßt amal wos des haßt. Und wennst mi no amoi anruafst loss i di vafuign über die Telefonleitung vo da Polizei. Vaschwind, wennst mi no amoi anruafst. Und wenn i di amoi siag, dann kriegst an Hokn von mir du Depperter.")

