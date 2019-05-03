from bittrex.bittrex import Bittrex

key = "e3f6f92870ac455ea973d29351fde495"
secret = "f0ef266e724147a1b3326ea74e0348eb"

api = Bittrex(api_key=key, api_secret=secret)

x = api.get_market_summaries()
print(x)
