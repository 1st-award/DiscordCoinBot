# -*- coding: utf-8 -*-
import requests
import json
from json import JSONDecodeError


# 환율
def usdtokrw():
    try:
        usdkrw = requests.get("https://api.manana.kr/exchange/rate/KRW/USD.json")
        usdkrw.encoding = "utf-8"
        usdkrw_data = json.loads(usdkrw.text)
        usdkrwrate = usdkrw_data[0]['rate']
        return usdkrwrate
    except JSONDecodeError as error:
        print(error)


# 코인 검색
def coin_search(coin):
    try:
        upbit_coin_raw = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-" + coin)
        upbit_coin_raw.encoding = "utf-8"
        upbit_coin_price = json.loads(upbit_coin_raw.text)
        upbit_coin_finalprice = upbit_coin_price[0]['trade_price']
        binance_coin_raw = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + coin.upper() + "USDT")
        binance_coin_raw.encoding = "utf-8"
        binance_coin_price = json.loads(binance_coin_raw.text)
        binance_coin_finalprice = float(binance_coin_price['price']) * usdtokrw()
        kimp_coin = upbit_coin_finalprice / binance_coin_finalprice * 100
        return kimp_coin
    except KeyError:
        return coin + "을(를) 찾을 수 없습니다."


# 코인 정보
def coin_information(coin):
    try:
        upbit_coin_raw = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-" + coin)
        upbit_coin_information = json.loads(upbit_coin_raw.text)
        coin_price = upbit_coin_information[0]['trade_price']
        coin_high_price = upbit_coin_information[0]['high_price']
        coin_low_price = upbit_coin_information[0]['low_price']
        coin_opening_price = upbit_coin_information[0]['opening_price']
        coin_highest_52_week_price = upbit_coin_information[0]['highest_52_week_price']
        coin_lowest_52_week_price = upbit_coin_information[0]['']
    except KeyError:
        return coin + "을(를) 찾을 수 없습니다."
