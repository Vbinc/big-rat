import pytest
from src.tradebook import Trade


def test_trade_json():
    trade = Trade()
    q = trade.json()
    assert trade.json() == '{"interest": "{\\"end\\": 0, \\"start\\": 0}", "potential": "{\\"end\\": 0, \\"start\\": 0}", "position": "{\\"direction\\": \\"LONG\\", \\"start\\": 0, \\"start_price\\": 0, \\"stop\\": 0, \\"stop_price\\": 0}"}'

def test_trade_write_tradebook():
    trade = Trade()
    assert trade.write_tradebook() == 'eJyrVsrMK0ktSi0uUbJSUKqOUUrNS4kBMg10FGKUiksSi0rAvFolHQWlgvyS1LySzMQcYpQWZ5Zk5udBVaZkFqUmg/ggFTFKPv5+7jFKqNrgvPiCoszkVCSx/AIUDpJ8rVItABbkOqM='

def test_trade_write_tradebook_compressed():
    trade = Trade()
    assert isinstance(trade.write_tradebook(use_compress=True, use_base64=False), bytes)

def test_trade_write_tradebook_compressed_and_encoded():
    trade = Trade()
    assert isinstance(trade.write_tradebook(use_compress=True, use_base64=True), str)
