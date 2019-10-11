import krakenex
import pprint
import json


k = krakenex.API()
k.load_key("kraken.key")


def SimpleTradeTest():
    response = k.query_private('AddOrder', {
        'pair': 'USDTZUSD',
        'type': 'buy',
        'ordertype': 'limit',
        'price': '1.0001',
        'volume': ' 10'
        # `ordertype`, `price`, `price2` are valid
        # 'close[ordertype]': 'limit',
        # 'close[price]': '9001',
        # these will be ignored!
        # 'close[pair]': 'XXBTZEUR',
        # 'close[type]': 'sell',
        # 'close[volume]': '1'
    })
    return response


def ListOpenOrder():
    res = k.query_private("OpenOrders")


def main():
    trade_results = SimpleTradeTest()
    open_orders = ListOpenOrder()

    res = {
        "trade_results": trade_results,
        "open_orders": open_orders
    }

    pprint.pprint(res)


main()
