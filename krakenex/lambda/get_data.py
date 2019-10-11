import krakenex
import pprint
import json

k = krakenex.API()
k.load_key("kraken.key")


def get_spot():
    tickers = k.query_public("Ticker", {"pair": "USDTZUSD,XLTCZUSD,XXBTZUSD"})
    result = tickers.get("result")
    
    dict(result)

    USDTZUSD_spot = result.get("USDTZUSD").get("c")[0]
    XLTCZUSD_spot = result.get("XLTCZUSD").get("c")[0]
    XXBTZUSD_spot = result.get("XXBTZUSD").get("c")[0]

    spot = {
    	"USDTZUSD_spot": USDTZUSD_spot,
    	"XLTCZUSD_spot": XLTCZUSD_spot,
		"XXBTZUSD_spot": XXBTZUSD_spot    	
    }
    return spot

def get_open_position():
	# req_data = {'docalcs': 'false'}
	# querry servers
	start = k.query_public('Time')
	open_positions = k.query_private('Balance')
	end = k.query_public('Time')
	latency = end['result']['unixtime']-start['result']['unixtime']

	dict(open_positions)

	if (open_positions["error"]):
		return_position = {
			"general_error": open_positions["error"][0]
		}		
		return return_position	
	
	return_position = {
		"error_count_postion": str(len(open_positions['error'])),
		"latency": str(latency),
		"balance": open_positions["result"]
	}
	return return_position

def ListOpenOrder():
	res = k.query_private("OpenOrders")

def main():
    spot = get_spot()
    return_position = get_open_position()
    open_orders = ListOpenOrder()
	# parse result
    output = {
		"spot": spot,
		"return_position": return_position,
		"open_orders": open_orders
    }
    pprint.pprint(output)
    # return output

main()
