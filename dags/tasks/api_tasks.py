def is_api_available():
    from coinmarketcapapi import CoinMarketCapAPI

    cmc = CoinMarketCapAPI()
    rep = cmc.cryptocurrency_info(symbol="BTC")
    assert type(rep.data) == dict
