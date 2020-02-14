import discord
from discord.ext import commands
import json
import os.path
import time

bot = commands.Bot(command_prefix=';')


async def createProfile(ctx):
    if ctx.message.mentions:
        profile = {
            "Discord id": ctx.message.mentions[0].id,
            "Discord name": ctx.message.mentions[0].name,
            "Time": 0,
            "Seconds": 0,
            "Minutes": 0,
            "Hours": 0,
            "Cookies": 0,
            "LastRedeemedDaily": 0,
            "LastRedeemedWeekly": 0,
            "LastRedeemedMonthly": 0
        }
        with open("profiles/" + str(ctx.message.mentions[0].id) + ".json", "w") as f:
            json.dump(profile, f, indent=4)
    else:
        profile = {
            "Discord id": ctx.author.id,
            "Discord name": ctx.author.name,
            "Time": 0,
            "Seconds": 0,
            "Minutes": 0,
            "Hours": 0,
            "Cookies": 0,
            "LastRedeemedDaily": 0,
            "LastRedeemedWeekly": 0,
            "LastRedeemedMonthly": 0
        }
        with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
            json.dump(profile, f, indent=4)


async def giveCurrency(ctx, time: 0, seconds: 0, minutes: 0, hours: 0, cookies: 0, showmessage: False):
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
            json.dump(profile, f, indent=4)
    if showmessage:
        gainEmbed = discord.Embed(title=ctx.author.name + " you gained:",
                             description="Time: " + str(time) + "\nSeconds: " + str(seconds) + "\nMinutes: " + str(minutes) + "\nHours: " + str(hours) + "\nCookies: " + str(cookies),
                             color=0xfeb647)
        await ctx.send(embed=gainEmbed)


@bot.command()
async def bal(ctx):
    profile = None
    print(ctx.message.mentions)
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        if not os.path.isfile("profiles/" + str(mentioned.id) + ".json"):
            await createProfile(ctx)
            with open("profiles/" + str(mentioned.id) + ".json", 'r+') as f:
                data = json.load(f)
                profile = {
                    "Discord id": mentioned.id,
                    "Discord name": mentioned.name,
                    "Time": data["Time"],
                    "Seconds": data["Seconds"],
                    "Minutes": data["Minutes"],
                    "Hours": data["Hours"],
                    "Cookies": data["Cookies"],
                    "LastRedeemedDaily": data["LastRedeemedDaily"],
                    "LastRedeemedWeekly": data["LastRedeemedWeekly"],
                    "LastRedeemedMonthly": data["LastRedeemedMonthly"]
                }
            balEmbed = discord.Embed(title=profile["Discord name"] + "'s balance:",
                                     description="Time: " + str(profile["Time"]) + "\nSeconds: " + str(
                                         profile["Seconds"]) + "\nMinutes: " + str(
                                         profile["Minutes"]) + "\nHours: " + str(
                                         profile["Hours"]) + "\nCookies: " + str(profile["Cookies"]),
                                     color=0xfeb647)
            await ctx.send(embed=balEmbed)
        else:
            with open("profiles/" + str(mentioned.id) + ".json", 'r+') as f:
                data = json.load(f)
                profile = {
                    "Discord id": mentioned.id,
                    "Discord name": mentioned.name,
                    "Time": data["Time"],
                    "Seconds": data["Seconds"],
                    "Minutes": data["Minutes"],
                    "Hours": data["Hours"],
                    "Cookies": data["Cookies"],
                    "LastRedeemedDaily": data["LastRedeemedDaily"],
                    "LastRedeemedWeekly": data["LastRedeemedWeekly"],
                    "LastRedeemedMonthly": data["LastRedeemedMonthly"]
                }
            balEmbed = discord.Embed(title=profile["Discord name"] + "'s balance:",
                                     description="Time: " + str(profile["Time"]) + "\nSeconds: " + str(
                                         profile["Seconds"]) + "\nMinutes: " + str(
                                         profile["Minutes"]) + "\nHours: " + str(
                                         profile["Hours"]) + "\nCookies: " + str(profile["Cookies"]),
                                     color=0xfeb647)
            await ctx.send(embed=balEmbed)
    else:
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
            balEmbed = discord.Embed(title=profile["Discord name"] + "'s balance:",
                                     description="Time: " + str(profile["Time"]) + "\nSeconds: " + str(
                                         profile["Seconds"]) + "\nMinutes: " + str(
                                         profile["Minutes"]) + "\nHours: " + str(
                                         profile["Hours"]) + "\nCookies: " + str(profile["Cookies"]),
                                     color=0xfeb647)
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
    print(abs(lastRedeemed - time.time()))

    if abs(lastRedeemed - time.time()) > 86400:
        await giveCurrency(ctx, 75, 0, 0, 0, 0, False)
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
                json.dump(profile, f, indent=4)
        dailyEmbed = discord.Embed(title=":calendar_spiral: Daily Redeem! :calendar_spiral:",
                                   description=f"{ctx.author.name} you recieved: +75 time!",color=0x33FFFF)
        await ctx.send(embed=dailyEmbed)
    else:
        dailyEmbed = discord.Embed(title=f"{ctx.author.name} you can't do that yet!",
                                   description="Try again later", color=0xFF5844)
        await ctx.send(embed=dailyEmbed)


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

    if abs(lastRedeemed - time.time()) > 604800:
        await giveCurrency(ctx, 200, 0, 0, 0, 0, False)
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
                json.dump(profile, f, indent=4)
        weeklyEmbed = discord.Embed(title=":calendar_spiral: Weekly Redeem! :calendar_spiral:",
                                    description=f"{ctx.author.name} you recieved: +200 time!",color=0x33FF99)
        await ctx.send(embed=weeklyEmbed)
    else:
        weeklyEmbed = discord.Embed(title=f"{ctx.author.name} you can't do that yet!",
                                   description="Try again later", color=0xFF5844)
        await ctx.send(embed=weeklyEmbed)


@bot.command()
async def monthly(ctx):
    lastRedeemed = None
    hasNotRedeemedOnce = False
    if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
        await createProfile(ctx)
    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        if not data["LastRedeemedWeekly"] is None:
            lastRedeemed = data["LastRedeemedMonthly"]
        else:
            hasNotRedeemedOnce = True

    if abs(lastRedeemed - time.time()) > 18144000:
        await giveCurrency(ctx, 725, 0, 0, 0, 0, False)
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
                "LastRedeemedMonthly": int(time.time())
            }
            with open("profiles/" + str(ctx.author.id) + ".json", "w") as f:
                json.dump(profile, f, indent=4)
        monthlyEmbed = discord.Embed(title=":calendar_spiral: MONTHLY Redeem! :calendar_spiral:",
                                     description=f"{ctx.author.name} you recieved: +725 time!",color=0x33FF00)
        await ctx.send(embed=monthlyEmbed)
    else:
        monthlyEmbed = discord.Embed(title=f"{ctx.author.name} you can't do that yet!",
                                     description="Try again later", color=0xFF5844)
        await ctx.send(embed=monthlyEmbed)
        
@bot.command()
async def give(ctx, mention, item, giveamount)
    with open("profiles/" + str(author.id) + ".json", 'r+') as f:
        data = json.load(f)
    with open("profiles/" + str(mentioned.id) + ".json", 'r+') as f:
        data = json.load(f)
	if data_author["Cookies"] > giveamount or data["cookies"] == giveamount:
        if not os.path.isfile("profiles/" + str(ctx.author.id) + ".json"):
            await createProfile(ctx)
            if not os.path.isfile("profiles/" + str(ctx.mention.id) + ".json"):
                await createProfile(ctx)
	else:
		print(f"You don't have enough {item}s!")

@bot.event
async def on_ready():
    print('Ready!')

bot.run('')
