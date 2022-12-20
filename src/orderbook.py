import base64
import time
import zlib
import jsons
from typing import Union

class OrderBook:
    """
    Order book for a pair of coins.
    ------------------
    
    Write .orderbook
    """

    def __init__(self, filename: str) -> None:
        """
        Create a new order book for a pair of coins.
        """
        self.filename = filename + '.orderbook'
        self.pair: str
        self.asks: dict[int, float]
        self.bids: dict[int, float]
        self.time = 0
        
    def add_asks(self, asks: dict[int, float]) -> None:
        """
        Add asks to the order book.
        """
        self.asks = asks
        
    def add_bids(self, bids: dict[int, float]) -> None:
        """
        Add bids to the order book.
        """
        self.bids = bids

    def write(self, file_name: str, use_compression=False, use_base64=False) -> Union[str, bytes]:
        if (not file_name.endswith('.orderbook')):
            file_name = file_name + '.orderbook'
            
        # convert to JSON string
        json_bytes = jsons.dumps(self, skipkeys=True)

        # compress and/or encode the bytes
        if use_compression:
            json_bytes = zlib.compress(json_bytes.encode())
            
        if use_base64:
            json_bytes = base64.b64encode(json_bytes if isinstance(json_bytes, bytes) else json_bytes.encode()).decode()
            
        self.asks = {}
        self.bids = {}
        self.time = 0

        # write the bytes to the file
        with open(file_name, 'a' if isinstance(json_bytes, str) else 'ab') as f:
            f.write(json_bytes)
            f.write('\n' if isinstance(json_bytes, str) else b'\n')

        return json_bytes
