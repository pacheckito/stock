from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # run a flask application 
                        # everytime we make a change to the code, the server will restart





"""import requests
import time 

ticker = "MSFT"
api_key = "b7bb1da24bfb4ed6a54a72dac148bb3d" #API key

def get_stock_price(ticker_symbol, api):
  url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
  response = requests.get(url).json()
  price = response['price'][:-3] # to strictly print the price with only 2 decimal places
  return price # print({ticker}, price)
  # print(price)
  
def get_stock_quote(ticker_symbol, api):
  url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
  response = requests.get(url).json()
  return response
  # print(response)

stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

stockdata = get_stock_quote(ticker, api_key)
name = stockdata['name']
volume = stockdata['volume']
open_price = stockdata['open']
close_price = stockdata['close']
low_price = stockdata['low']
high_price = stockdata['high']
exchange = stockdata['exchange']
currency = stockdata['currency']

print(name,":",stock_price)"""