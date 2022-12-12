import pytest
from src.OrderBook import OrderBook

# create a test OrderBook instance
@pytest.fixture
def order_book():
    return OrderBook('test_order_book')

def test_init(order_book):
    # test that the filename attribute is set correctly
    assert order_book.filename == 'test_order_book.orderbook'

    # test that the pair attribute is set correctly
    assert order_book.pair == 'BTC/USDT'

    # test that the asks attribute is set correctly
    assert order_book.asks == {}

    # test that the bids attribute is set correctly
    assert order_book.bids == {}

    # test that the time attribute is set correctly
    assert order_book.time == 0

def test_write_with_compression(order_book: OrderBook):
    # test that the write method compresses the data when use_compression is set to True
    json_bytes = order_book.write(file_name="test1", use_compression=True)
    assert isinstance(json_bytes, bytes)

def test_write_with_base64_encoding(order_book: OrderBook):
    # test that the write method encodes the data with base64 when use_base64 is set to True
    json_string: str|bytes = order_book.write(file_name="test2", use_base64=True)
    assert isinstance(json_string, str)

def test_write_with_compression_and_base64_encoding(order_book: OrderBook):
    # test that the write method compresses and encodes the data when use_compression and use_base64 are set to True
    json_string: str|bytes = order_book.write(file_name="test3", use_compression=False, use_base64=False)
    assert isinstance(json_string, str)