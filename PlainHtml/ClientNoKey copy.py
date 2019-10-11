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

#Historical Data Initialization
#wb = xlwings.Book('Historical Data.xlsx')
#DataSheet = wb.sheets['Monitor']
#RowNum = 1
#ColNum = 1

#初始化apikey，secretkey,url
apikey = ''
secretkey = ''
okcoinRESTURL = 'www.okex.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
#Load Spot last/bid/ask
#print (u' 期货市场深度信息')
#Fut_Data =okcoinFuture.future_depth('btc_usd','this_week','6')
#Fut_Ask=Fut_Data.get("asks")
#print (Fut_Ask)

#Load next week fut spot/bid/last
print (u' 期货行情信息')
while True:
    try:
        Fut_Data_Next_Quarter_BTC = okcoinFuture.future_ticker('btc_usd','quarter')
        Fut_Data_Next_Quarter_LTC = okcoinFuture.future_ticker('ltc_usd','quarter')
        LTC_Index = okcoinFuture.future_index('ltc_usd')
        BTC_Index = okcoinFuture.future_index('btc_usd')
        USDT_Index = okcoinFuture.exchange_rate()
        LTC_Fut_Pos = json.loads(okcoinFuture.future_position('ltc_usd','quarter')).get('holding')[0].get('sell_amount')
        BTC_Fut_Pos = json.loads(okcoinFuture.future_position('btc_usd','quarter')).get('holding')[0].get('sell_amount')
        Total_Pos = json.loads(okcoinFuture.future_userinfo())
        BTC_Spot_OKCoin = okcoinSpot.ticker('btc_usdt').get('ticker').get('last')
        LTC_Spot_OKCoin = okcoinSpot.ticker('ltc_usdt').get('ticker').get('last')
        #USDT_Spot_OKCoin
        
    except:
        time.sleep(3)
        continue
    else:
        Spot_Price_BTC = BTC_Index["future_index"]
        Spot_Price_LTC = LTC_Index["future_index"]
        Spot_Price_USD = USDT_Index["rate"]
        Fut_Next_Quarter_LTC = float(Fut_Data_Next_Quarter_LTC.get("ticker").get("last"))
        Fut_Next_Quarter_BTC = float(Fut_Data_Next_Quarter_BTC.get("ticker").get("last"))
        #Compute Basis
        
        print (u' LTC Basis Quarter')
        Last_Basis_Quarter_LTC = Fut_Next_Quarter_LTC / Spot_Price_LTC -1
        print(Last_Basis_Quarter_LTC)
        print (u' BTC Basis Quarter')
        Last_Basis_Quarter_BTC = Fut_Next_Quarter_BTC / Spot_Price_BTC -1
        print(Last_Basis_Quarter_BTC)
        
        #Write into Excel for Historical Data
        #DataSheet.range(RowNum,ColNum).value = [datetime.datetime.now(),Last_Basis_Quarter_BTC]
        #DataSheet.range(RowNum,ColNum+2).value = [datetime.datetime.now(),Last_Basis_Quarter_LTC]
        RowNum = RowNum+1
        LTC_Spot_Pos = Total_Pos.get('info').get('ltc').get('account_rights')
        BTC_Spot_Pos = Total_Pos.get('info').get('btc').get('account_rights')
        print (u'获取全仓持仓信息')
        print (BTC_Fut_Pos)
        
        #Print index prices and Spot USDT prices for manual trading
        #DataSheet.range(1,5).value = ['LTC Index',Spot_Price_LTC]
        #DataSheet.range(1,7).value = ['BTC Index',Spot_Price_BTC]
        #DataSheet.range(16,7).value= LTC_Spot_OKCoin
        #DataSheet.range(21,7).value= BTC_Spot_OKCoin
        
        #print futures prices for manual trading
        #DataSheet.range(15,8).value = Fut_Next_Quarter_LTC
        #DataSheet.range(20,8).value = Fut_Next_Quarter_BTC
        
        #Print current Spot and futures position for position keeping and PnL tracking
        #DataSheet.range(15,6).value=LTC_Fut_Pos*10/Spot_Price_LTC
        #DataSheet.range(20,6).value=BTC_Fut_Pos*100/Spot_Price_BTC
        #DataSheet.range(15,5).value=LTC_Spot_Pos
        #DataSheet.range(20,5).value=BTC_Spot_Pos
        break
        time.sleep(60)
#Trading Portion, STILL UNDER TESTING
#print (okcoinFuture.future_trade('ltc_usd','this_quarter','0.1','1','1','0','10'))        
#get order_id, get result
        
    


#print (u'获取预估交割价') 
#time.sleep(10)
#print (okcoinFuture.future_estimated_price('btc_usd'))

#print (u' 期货行情信息')
#print (okcoinFuture.future_ticker('ltc_usd','this_week'))
#Future_Data = okcoinFuture.future_ticker('btc_usd','next_week')
#print (Future_Data)



#print (u'期货交易记录信息') 
#print (okcoinFuture.future_trades('ltc_usd','this_week'))

#print (u'期货指数信息')
#print (okcoinFuture.future_index('ltc_usd'))

#print (u'美元人民币汇率')
#print (okcoinFuture.exchange_rate())

#print (u'获取预估交割价') 
#print (okcoinFuture.future_estimated_price('ltc_usd'))

#print (u'获取全仓账户信息')
#print (okcoinFuture.future_userinfo())

#print (u'获取全仓持仓信息')
#print (okcoinFuture.future_position('ltc_usd','this_week'))

#print (u'期货下单')
#print (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

#print (u'期货批量下单')
#print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'期货取消订单')
#print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

#print (u'期货获取订单信息')
#print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

#print (u'期货逐仓账户信息')
#print (okcoinFuture.future_userinfo_4fix())

#print (u'期货逐仓持仓信息')
#print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))

