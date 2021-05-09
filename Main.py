# -*- coding: utf-8 -*-
import asyncio
import discord
import os
import platform
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
from kimp import *

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!', intents=intents)
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
json_file_name = ''
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = ''
doc = gc.open_by_url(spreadsheet_url)


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
    count_server = worksheet.acell('I2').value
    worksheet.update_acell('A' + count_server, str(guild.owner_id))
    worksheet.update_acell('B' + count_server, str(guild.text_channels[0].id))
    worksheet.update_acell('C' + count_server, str(0))
    worksheet.update_acell('I' + count_server, str(int(count_server)+1))
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('코인 봇이 참가하였습니다. 명령어는 !help입니다.', delete_after=10.0)
        break


# 김프 상태 확인
async def change_reference():
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
async def ping(ctx):
    print('success')
    print(ctx.message.author.id)
    print(ctx.message.guild.id)
    await ctx.send('Pong', delete_after=3.0)


bot.run('')
