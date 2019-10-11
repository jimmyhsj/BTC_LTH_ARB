from OkcoinFutureAPI import OKCoinFuture
from OkcoinSpotAPI import OKCoinSpot
import time
#import xlwings
import datetime
import json
import pprint

apikey = 'cb8450d0-04e3-4f40-b1a5-3f9313e8d522'
secretkey = '76E0A031432B6546E5255C3D1B3A7810'
okcoinRESTURL = 'www.okex.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn  
# okcoinRESTURL = '47.90.110.144'

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
results = {}

	

def main():
	# spot_position = okcoinSpot.userinfo()
	# future_position = okcoinFuture.future_userinfo()
	# test_ticker = okcoinFuture.future_depth('btc_usd','this_week','6')
	
	
	
	# print (okcoinFuture.future_estimated_price('ltc_usd'))

	# print (okcoinFuture.future_depth('btc_usd','this_week','6'))
	# print (okcoinFuture.exchange_rate())
	# print (okcoinFuture.future_ticker('ltc_usd','this_week'))
	pprint.pprint(okcoinFuture.future_userinfo())
	
	# results = {
	# # 'spot_position': spot_position,
	# # 'future_position': future_position
	# 'test_ticker': test_ticker,
	# 'test2_ticker': okcoinFuture.future_ticker('ltc_usd','this_week')
	# }
	# pprint.pprint(results)

main()