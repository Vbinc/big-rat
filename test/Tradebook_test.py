import pytest
from src.TradeBook import Trade

# create a test Trade instance
@pytest.fixture
def trade():
    return Trade(interest=(1, 2), potential=(3, 4), position=(5, 6, True))

def test_init(trade: Trade):
    # test that the interest attribute is set correctly
    assert trade.interest == (1, 2)

    # test that the potential attribute is set correctly
    assert trade.potential == (3, 4)

    # test that the position attribute is set correctly
    assert trade.position == (5, 6, True)

def test_update_interest(trade: Trade):
    # test that the update_interest method updates the interest attribute correctly
    trade.update_interest(start=10, end=20)
    assert trade.interest == (10, 20)

def test_update_potential(trade: Trade):
    # test that the update_potential method updates the potential attribute correctly
    trade.update_potential(start=30, end=40)
    assert trade.potential == (30, 40)

def test_update_position(trade: Trade):
    # test that the update_position method updates the position attribute correctly
    trade.update_position(start=50, end=60, isLong=False)
    assert trade.position == (50, 60, False)

def test_write_tradebook(trade: Trade):
    # test that the write_tradebook method returns the expected string
    assert trade.write(use_compress=False, use_base64=False) == '{"interest": [1, 2], "position": [5, 6, true], "potential": [3, 4]}'

def test_write_tradebook_with_compression(trade: Trade):
    # test that the write_tradebook method compresses the data when use_compress is set to True
    json_bytes = trade.write(use_compress=True, use_base64=False)
    assert isinstance(json_bytes, bytes)

def test_write_tradebook_with_base64_encoding(trade: Trade):
    # test that the write_tradebook method encodes the data with base64 when use_base64 is set to True
    json_string = trade.write(use_compress=False, use_base64=True)
    assert isinstance(json_string, str)
    
def test_write_tradebook_with_compression_and_base64_encoding(trade: Trade):
    # test that the write_tradebook method compresses and encodes the data with base64 when use_compress and use_base64 are set to True
    json_bytes = trade.write(use_compress=True, use_base64=True)
    assert isinstance(json_bytes, str)
