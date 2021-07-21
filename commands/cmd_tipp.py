import csv
import random


async def ex(args, message):
    with open("/commands/data/results.csv", 'r', encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        sum1 = 294970
        sum2 = 0
        key = random.randint(0, sum1)
        print(key)
        for line in csv_reader:
            result = line["result"]
            times = int(line["times"])

            sum2 += times

            if sum2 >= key:
                print(result)
                break
    output = ' '.join(args)
    output += "\n"
    output += result
    await message.channel.send(output)
