from coinmarketcapapi import CoinMarketCapAPI
from requests import Request, Session
import json

def _is_api_available():
    cmc = CoinMarketCapAPI()
    rep = cmc.cryptocurrency_info(symbol="BTC")
    assert type(rep.data) == dict

def _get_json_response_from_api():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    parameters = {
        "symbol": "BTC",
        "convert": "USD"
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "ed37ffef-4feb-44a4-82c7-950ef54862ad"
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    btc_price = json.loads(response.text)["data"]["BTC"]["quote"]["USD"]["price"]
    btc_symbol = json.loads(response.text)["data"]["BTC"]["symbol"]
    print(f"Btc current price: {btc_price}")