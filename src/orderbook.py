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

    def write(self, file_name=None, use_compression=True, use_base64=True) -> Union[str, bytes]:
        if file_name is None:
            file_name = self.pair.__str__() + str(int(time.time())) + ".orderbook"

        # convert to JSON string
        json_bytes = jsons.dumps(self, skipkeys=True).encode('utf-8')

        # compress and/or encode the bytes
        if use_compression and use_base64:
            # compress and encode the bytes
            json_bytes = zlib.compress(json_bytes)
            json_bytes = base64.b64encode(json_bytes).decode('utf-8')
        elif use_compression:
            # compress the bytes
            json_bytes = zlib.compress(json_bytes)
        elif use_base64:
            # encode the bytes
            json_bytes = base64.b64encode(json_bytes).decode('utf-8')

        # write the bytes to the file
        if isinstance(json_bytes, str):
            with open(file_name, "a") as file:
                file.writelines([json_bytes])
            return json_bytes
        elif isinstance(json_bytes, bytes):
            with open(file_name, "ab") as file:
                file.writelines([json_bytes])
            return json_bytes

        return json_bytes
