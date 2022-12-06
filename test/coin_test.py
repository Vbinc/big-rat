import pytest
from src.coin import Coin

def test_coin():
    coin = Coin("BTC", "Bitcoin")
    assert coin.ticker == "BTC"
    assert coin.name == "Bitcoin"
    assert str(coin) == "BTC"
    

