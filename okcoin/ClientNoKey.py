#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinFutureAPI import OKCoinFuture
from OkcoinSpotAPI import OKCoinSpot
import time
#import xlwings
import datetime
import json


apikey = ''
secretkey = ''
okcoinRESTURL = 'www.okex.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
results = {}

def main():
    try:
        BTC_Spot_OKCoin = okcoinSpot.ticker('btc_usdt').get('ticker').get('last')
        LTC_Spot_OKCoin = okcoinSpot.ticker('ltc_usdt').get('ticker').get('last')
        BCH_Spot_OKCoin = okcoinSpot.ticker('bch_usdt').get('ticker').get('last')
        
        Fut_Data_This_Week_BTC = float(okcoinFuture.future_ticker('btc_usd','this_week').get("ticker").get("last"))
        Fut_Data_This_Week_LTC = float(okcoinFuture.future_ticker('ltc_usd','this_week').get("ticker").get("last"))
        Fut_Data_This_Week_BCH = float(okcoinFuture.future_ticker('bch_usd','this_week').get("ticker").get("last"))
        
        Fut_Data_Next_Week_BTC = float(okcoinFuture.future_ticker('btc_usd','next_week').get("ticker").get("last"))
        Fut_Data_Next_Week_LTC = float(okcoinFuture.future_ticker('ltc_usd','next_week').get("ticker").get("last"))
        Fut_Data_Next_Week_BCH = float(okcoinFuture.future_ticker('bch_usd','next_week').get("ticker").get("last"))
        
        Fut_Data_Next_Quarter_LTC = float(okcoinFuture.future_ticker('ltc_usd','quarter').get("ticker").get("last"))
        Fut_Data_Next_Quarter_BTC = float(okcoinFuture.future_ticker('btc_usd','quarter').get("ticker").get("last"))
        Fut_Data_Next_Quarter_BCH = float(okcoinFuture.future_ticker('bch_usd','quarter').get("ticker").get("last"))
        
        LTC_Index = okcoinFuture.future_index('ltc_usd').get("future_index")
        BTC_Index = okcoinFuture.future_index('btc_usd').get("future_index")
        BCH_Index = okcoinFuture.future_index('bch_usd').get("future_index")
        USDT_Index = okcoinFuture.exchange_rate().get("rate")
        
    except (RuntimeError):
        raise RuntimeError
        
    results = {
        'BTC_Spot_OKCoin': BTC_Spot_OKCoin, 'LTC_Spot_OKCoin': LTC_Spot_OKCoin, 'BCH_Spot_OKCoin':BCH_Spot_OKCoin,
        'BTC_Index': BTC_Index, 'LTC_Index': LTC_Index, 'BCH_Index': BCH_Index, 'USDT_Index': USDT_Index,
        'Fut_Data_This_Week_BTC': Fut_Data_This_Week_BTC, 'Fut_Data_This_Week_LTC': Fut_Data_This_Week_LTC, 'Fut_Data_This_Week_BCH': Fut_Data_This_Week_BCH,
        'Fut_Data_Next_Week_BTC': Fut_Data_Next_Week_BTC, 'Fut_Data_Next_Week_LTC': Fut_Data_Next_Week_LTC, 'Fut_Data_Next_Week_BCH': Fut_Data_Next_Week_BCH,
        'Fut_Data_Next_Quarter_BTC': Fut_Data_Next_Quarter_BTC, 'Fut_Data_Next_Quarter_LTC': Fut_Data_Next_Quarter_LTC, 'Fut_Data_Next_Quarter_BCH': Fut_Data_Next_Quarter_BCH,
    }
    print(results)
    return results

main()