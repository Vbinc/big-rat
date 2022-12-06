import pytest
from src.coin import Coin
from src.indicators import Indicator
from src.pair import TradePair

def test_indicator_with_tradepair():
    """Test the Indicator class with a TradePair"""
    indicator = Indicator("test", TradePair(Coin("BTC", "Bitcoin"), Coin("USDT", "Tether USD")), 0, 0)
    assert indicator.pair.coin_a.ticker == "BTC"
    assert indicator.pair.coin_b.ticker == "USDT"
