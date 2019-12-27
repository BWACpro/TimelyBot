import discord
from discord.ext import commands
import json
import os.path
import time

bot = commands.Bot(command_prefix=':')


async def createProfile(ctx):
    profile = {
        "Discord id": ctx.author.id,
        "Discord name": ctx.author.name,
        "Time": 0,
        "Seconds": 0,
        "Minutes": 0,
        "Hours": 0,
        "Cookies": 0,
        "LastRedeemedDaily": 99999999999999,
        "LastRedeemedWeekly": 999999999999999,
        "LastRedeemedMonthly": 99999999999999
    }
    with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
        json.dump(profile, file, indent=4)


async def giveCurrency(ctx, time: 0, seconds: 0, minutes: 0, hours: 0, cookies: 0):
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        profile = {
            "Discord id": ctx.author.id,
            "Discord name": ctx.author.name,
            "Time": data["Time"] + int(time),
            "Seconds": data["Seconds"] + int(seconds),
            "Minutes": data["Minutes"] + int(minutes),
            "Hours": data["Hours"] + int(hours),
            "Cookies": data["Cookies"] + int(cookies),
            "LastRedeemedDaily": data["LastRedeemedDaily"],
            "LastRedeemedWeekly": data["LastRedeemedWeekly"],
            "LastRedeemedMonthly": data["LastRedeemedMonthly"]
        }
        with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
            json.dump(profile, file, indent=4)
    gainEmbed = discord.Embed(title=ctx.author.name + " you gained:",
                         description="Time: " + str(time) + "\nSeconds: " + str(seconds) + "\nMinutes: " + str(minutes) + "\nHours: " + str(hours) + "\nCookies: " + str(cookies),
                         color=0xe8d01e)
    await ctx.send(embed=gainEmbed)


@bot.command()
async def bal(ctx):
    profile = None
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        profile = {
            "Discord id": ctx.author.id,
            "Discord name": ctx.author.name,
            "Time": data["Time"],
            "Seconds": data["Seconds"],
            "Minutes": data["Minutes"],
            "Hours": data["Hours"],
            "Cookies": data["Cookies"],
            "LastRedeemedDaily": data["LastRedeemedDaily"],
            "LastRedeemedWeekly": data["LastRedeemedWeekly"],
            "LastRedeemedMonthly": data["LastRedeemedMonthly"]
        }

    balEmbed = discord.Embed(title="Your balance:",
                         description="Time: " + str(profile["Time"]) + "\nSeconds: " + str(profile["Seconds"]) + "\nMinutes: " + str(profile["Minutes"]) + "\nHours: " + str(profile["Hours"]) + "\nCookies: " + str(profile["Cookies"]),
                         color=0xe8d01e)
    await ctx.send(embed=balEmbed)


@bot.command()
async def daily(ctx):
    lastRedeemed = None
    hasNotRedeemedOnce = False
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        if not data["LastRedeemedDaily"] is None:
            lastRedeemed = data["LastRedeemedDaily"]
        else:
            hasNotRedeemedOnce = True

    if lastRedeemed - time.time() > 86400:
        await giveCurrency(ctx, 75, 0, 0, 0, 0)
        with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
            data = json.load(f)
            profile = {
                "Discord id": ctx.author.id,
                "Discord name": ctx.author.name,
                "Time": data["Time"],
                "Seconds": data["Seconds"],
                "Minutes": data["Minutes"],
                "Hours": data["Hours"],
                "Cookies": data["Cookies"],
                "LastRedeemedDaily": int(time.time()),
                "LastRedeemedWeekly": data["LastRedeemedWeekly"],
                "LastRedeemedMonthly": data["LastRedeemedMonthly"]
            }
            with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
                json.dump(profile, file, indent=4)
        await ctx.send("come back tomorrow")
    else:
        await ctx.send("you cant do that yet")


@bot.command()
async def weekly(ctx):
    lastRedeemed = None
    hasNotRedeemedOnce = False
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        if not data["LastRedeemedWeekly"] is None:
            lastRedeemed = data["LastRedeemedWeekly"]
        else:
            hasNotRedeemedOnce = True

    if lastRedeemed - time.time() > 604800:
        await giveCurrency(ctx, 200, 0, 0, 0, 0)
        with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
            data = json.load(f)
            profile = {
                "Discord id": ctx.author.id,
                "Discord name": ctx.author.name,
                "Time": data["Time"],
                "Seconds": data["Seconds"],
                "Minutes": data["Minutes"],
                "Hours": data["Hours"],
                "Cookies": data["Cookies"],
                "LastRedeemedDaily": data["LastRedeemedDaily"],
                "LastRedeemedWeekly": int(time.time()),
                "LastRedeemedMonthly": data["LastRedeemedMonthly"]
            }
            with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
                json.dump(profile, file, indent=4)
        await ctx.send("come back next week")
    else:
        await ctx.send("you cant do that yet")


@bot.command()
async def monthly(ctx):
    lastRedeemed = None
    hasNotRedeemedOnce = False
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        if not data["LastRedeemedWeekly"] is None:
            lastRedeemed = data["LastRedeemedMonthly”]
        else:
            hasNotRedeemedOnce = True

    if lastRedeemed - time.time() > 18144000:
        await giveCurrency(ctx, 750, 0, 0, 0, 0)
        with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
            data = json.load(f)
            profile = {
                "Discord id": ctx.author.id,
                "Discord name": ctx.author.name,
                "Time": data["Time"],
                "Seconds": data["Seconds"],
                "Minutes": data["Minutes"],
                "Hours": data["Hours"],
                "Cookies": data["Cookies"],
                "LastRedeemedDaily": data["LastRedeemedDaily"],
                "LastRedeemedWeekly": data["LastRedeemedWeekly”],
                "LastRedeemedMonthly": int(time.time())
            }
            with open("profiles/" + str(ctx.author.id) + ".json", "w") as file:
                json.dump(profile, file, indent=4)
        await ctx.send("Come back next month!")
    else:
        await ctx.send("You cant do that yet!")

bot.run('InsertBotToken')
