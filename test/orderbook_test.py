import pytest

from src.coin import Coin
from src.orderbook import OrderBook
from src.pair import TradePair


def test_orderbook():
    # create a pair of coins and an order book
    pair = TradePair(Coin("BTC", "Bitcoin"), Coin("USDT", "Tether USD"))
    orderbook = OrderBook(pair)

    # set the asks and bids for the order book
    asks: dict[int, float] = {1000: 10, 1001: 11, 1002: 12}
    bids: dict[int, float] = {999: 9, 998: 8, 997: 7}
    orderbook.set_asks(asks)
    orderbook.set_bids(bids)

    # check that the order book's asks and bids are set correctly
    assert orderbook.asks == asks
    assert orderbook.bids == bids

    # write the order book to a file and check that the file is written correctly
    compressed = orderbook.write("orderbook.txt", use_compression=False, use_base64=False)
    assert compressed == b'{"asks": {"1000": 10, "1001": 11, "1002": 12}, "bids": {"999": 9, "998": 8, "997": 7}, "pair": {"coin_a": {"name": "Bitcoin", "ticker": "BTC"}, "coin_b": {"name": "Tether USD", "ticker": "USDT"}}}'
    
    compressed = orderbook.write("orderbook.txt", use_compression=True, use_base64=False)
    assert compressed == b'x\x9cU\xcb1\x0e\xc20\x0c\x85\xe1\xabD\x9e\x19\x92.\xad\x19\x81\x1b\x10f\x94\x96HX\x15\x05\xa5\xd9\xaa\xdc\x9dgw\xea\x94/O\xbf7J\xeb\xbc\xd2\xd9m\x14\xbc\xf7@\xf0\'\xa7\x0e\xea\xb0\xbbSw\r\x9fQ^{\xcd\xccx\x19\x13\xf3\x00\r\xa6\x1e\xea\xb5\xfb%)\xd6M_Y\x9e\xc9\xb8\xa4O\x06\xe8"UWBVe\x9as\xb11^I\x0f\xad\x1f\x0f}\xcc\xf5\x9d\x8b{\xdco\xc7\x13\x0c\x91Zk\x7fE/3S'
    
    base64 = orderbook.write("orderbook.txt", use_compression=False, use_base64=True)
    assert base64 == "eyJhc2tzIjogeyIxMDAwIjogMTAsICIxMDAxIjogMTEsICIxMDAyIjogMTJ9LCAiYmlkcyI6IHsiOTk5IjogOSwgIjk5OCI6IDgsICI5OTciOiA3fSwgInBhaXIiOiB7ImNvaW5fYSI6IHsibmFtZSI6ICJCaXRjb2luIiwgInRpY2tlciI6ICJCVEMifSwgImNvaW5fYiI6IHsibmFtZSI6ICJUZXRoZXIgVVNEIiwgInRpY2tlciI6ICJVU0RUIn19fQ=="
    
    full = orderbook.write("orderbook.txt", use_compression=True, use_base64=True)
    assert full == "eJxVyzEOwjAMheGrRJ4Zki6tGYEbEGaUlkhYFQWl2arcnWd36pQvT783Suu80tltFLz3QPAnpw7qsLtTdw2fUV57zcx4GRPzAA2mHuq1+yUp1k1fWZ7JuKRPBugiVVdCVmWac7ExXkkPrR8Pfcz1nYt73G/HEwyRWmt/RS8zUw=="
