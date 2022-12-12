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

    def __init__(self, filename: str, pair: str = "BTC/USDT", asks: dict[int, float] = {}, bids: dict[int, float] = {}, time: int = 0) -> None:
        """
        Create a new order book for a pair of coins.
        """
        self.filename = filename + '.orderbook'
        self.pair = pair
        self.asks: dict[int, float] = asks
        self.bids: dict[int, float] = bids
        self.time = time

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
            f.writelines([json_bytes])

        return json_bytes
