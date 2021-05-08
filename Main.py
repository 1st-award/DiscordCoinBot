# -*- coding: utf-8 -*-
import asyncio
import discord
import os
import platform
from discord.ext import commands
from kimp import *

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!', intents=intents)


# 봇 준비
@bot.event
async def on_ready():
    print(f"봇 이름: {bot.user.name}")
    print(f"디스코드 API 버전: {discord.__version__}")
    print(f"파이썬 버전: {platform.python_version()}")
    print(f"시스템 사양: {platform.system()} {platform.release()} {os.name}")
    for guilds in bot.guilds:
        print(str(guilds.owner_id))
    print("-" * 30)
    bot.loop.create_task(changeReference())


# 김프 상태 확인
async def changeReference():
    coinType = ["btc", "etc", "eth", "xrp", "trx"]
    try:
        for coin in coinType:
            await bot.change_presence(activity=discord.Game(name=coin.upper()+": "+str(round(coinSearch(coin)))+"%"))
            await asyncio.sleep(5)
    except Exception as error:
        print(error)
        pass


# Test
@bot.command()
async def Ping(ctx):
    print('success')
    print(ctx.message.author.id)
    print(ctx.message.guild.id)
    await ctx.send('Pong', delete_after=3.0)


# 절대로 토큰을 넣어둔 체 푸시 하지 말 것!
access_token = os.environ['BOT_TOKEN']
bot.run(access_token)
