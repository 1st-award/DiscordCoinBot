# -*- coding: utf-8 -*-
import discord
import os
import platform
from discord.ext import commands
from FoodSelect import *

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


# Test
@bot.command()
async def Ping(ctx):
    print('success')
    print(ctx.message.author.id)
    print(ctx.message.guild.id)
    await ctx.send('Pong', delete_after=3.0)


# 점심 선택 장애 해결자
@bot.command()
async def 뭐먹지(ctx):
    await ctx.message.delete()
    removePrefixInMessage = ctx.message.content.replace("!뭐먹지 ", "")  # 클라이언트의 메세지에서 !뭐먹지를 제거
    inCommand = removePrefixInMessage.split()
    if inCommand[0] in "추가":
        await ctx.send(addFood(inCommand[1]), delete_after=3.0)
    elif inCommand[0] in "제거":
        await ctx.send(removeFood(inCommand[1]), delete_after=3.0)
    else:
        await ctx.send(Choice(), delete_after=5.0)


# 절대로 토큰을 넣어둔 체 푸시 하지 말 것!
access_token = os.environ['BOT_TOKEN']
bot.run(access_token)
