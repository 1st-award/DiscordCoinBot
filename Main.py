# -*- coding: utf-8 -*-
import asyncio
import discord
import os
import platform
from discord.ext import commands
from server_send import *
from kimp import *


# 봇 권한 부여
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
    bot.loop.create_task(change_reference())


@bot.event
async def on_guild_join(guild):
    # from server_send.py
    guild_join(guild)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('코인 봇이 참가하였습니다. 명령어는 !help입니다.', delete_after=10.0)
        break


# 명령어가 성공했을 때 로그에 전송
@bot.event
async def on_command_completion(ctx):
    full_command_name = ctx.command.qualified_name
    split = full_command_name.split(" ")
    executed_command = str(split[0])
    # from server_send.py
    log('INFO', executed_command, ctx.guild.name,
        str(ctx.message.guild.id), str(ctx.message.author), str(ctx.message.author.id))


# 김프 상태 확인
async def change_reference():
    coinType = ["btc", "etc", "eth", "xrp", "trx"]
    try:
        for coin in coinType:
            await bot.change_presence(activity=discord.Game(name=coin.upper()+": "+str(round(coin_search(coin)))+"%"))
            await asyncio.sleep(5)
    except Exception as error:
        print(error)
        pass


# Test
@bot.command()
async def ping(ctx):
    print('success')
    print(ctx.message.author.id)
    print(ctx.message.guild.id)
    await ctx.send('Pong', delete_after=3.0)


# 올릴 때 삭제
bot.run('NDcyOTgxMTM4NjEzNDY5MTg0.W11AAw.bk4e9onJ8ERO8VWCSNbRJTchsFs')
