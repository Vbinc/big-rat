import pytest
from src.coin import Coin
from src.indicators import Indicator
from src.pair import TradePair

def test_indicator():
    indicator1 = Indicator("test", TradePair(
        coin_a=Coin("BTC", "Bitcoin"), 
        coin_b=Coin("USDT", "Tether USD")), 
        1, 1)
    indicator1.set_value(2)
    assert indicator1.get_value() == 2


def test_indicator2():
    indicator1 = Indicator("test", TradePair(
        coin_a=Coin("BTC", "Bitcoin"), 
        coin_b=Coin("USDT", "Tether USD")), 
        1)
    indicator1.set_time_unix(2)
    assert indicator1.get_time_unix() == 2


def test_indicator3():
    indicator1 = Indicator("test", TradePair(
        coin_a=Coin("BTC", "Bitcoin"), 
        coin_b=Coin("USDT", "Tether USD")), 
        1)
    indicator1.set_indicator(2, 2)
    assert indicator1.get_value() == 2
    assert indicator1.get_time_unix() == 2
