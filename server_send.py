# -*- coding: utf-8 -*-
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 구글 스프레드 시트 연결
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
json_file_name = 'discordcoinbot-094ab3cac145.json'  # 올릴 때 삭제
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
# 올릴 때 삭제
coin_server_url = 'https://docs.google.com/spreadsheets/d/1ooI25uDwB6p8_Okeek_vjeU4Fl4dIJY8AscSO2nZ_Oc/edit#gid=0'
# 스프레스시트 문서 가져오기
server_doc = gc.open_by_url(coin_server_url)
# 시트 선택하기
server_worksheet = server_doc.worksheet('serverInformation')
log_worksheet = server_doc.worksheet('serverLog')


# 시간 얻기
def date():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')


def time():
    now = datetime.datetime.now()
    return now.strftime('%H:%M:%S')


# 길드에 들어 올 때
def guild_join(guild):
    server_count = int(server_worksheet.acell('J1').value)
    server_worksheet.insert_row([str(guild.owner.id), str(guild.text_channels[0].id), '0'], server_count)
    server_worksheet.update_acell('J1', server_count + 1)


# 명령어 성공 했을 때
def log(type, executed_command, guild_name, guild_id, author, author_id):
    count_server = int(log_worksheet.acell('J1').value)
    log_worksheet.insert_row(
        [type, date(), time(), executed_command, guild_name, guild_id, author, author_id], count_server)
    log_worksheet.update_acell('J1', count_server + 1)

# def fail_log():
