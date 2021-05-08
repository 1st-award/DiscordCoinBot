import requests
import json


def usdtokrw():
    usdkrw = requests.get("https://api.manana.kr/exchange/rate/KRW/USD.json")
    usdkrw_data = json.loads(usdkrw.text)
    usdkrwrate = usdkrw_data[0]['rate']
    return usdkrwrate


def coinSearch(coin):
    try:
        upbit_coin_raw = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-" + coin)
        upbit_coin_price = json.loads(upbit_coin_raw.text)
        upbit_coin_finalprice = upbit_coin_price[0]['trade_price']
        binance_coin_raw = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + coin.upper() + "USDT")
        binance_coin_price = json.loads(binance_coin_raw.text)
        binance_coin_finalprice = float(binance_coin_price['price']) * usdtokrw()
        kimp_coin = upbit_coin_finalprice / binance_coin_finalprice * 100
        return kimp_coin
    except KeyError:
        return coin + "을(를) 찾을 수 없습니다."
