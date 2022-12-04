import base64
import time
import zlib
import jsons
from coin import Coin
from pair import TradePair

class OrderBook:
    """
    Order book for a pair of coins.
    """
    pair = TradePair(Coin("BTC", "Bitcoin"), Coin("USDT", "Tether USD"))
    asks: dict = {}
    bids: dict = {}

    def __init__(self, pair: TradePair):
        """
        Create a new order book for a pair of coins.
        """
        self.pair = pair
        self.asks: dict = {}
        self.bids: dict = {}

    def set_asks(self, asks: dict):
        """
        Set the asks for the order book.
        """
        self.asks = asks

    def set_bids(self, bids: dict):
        """
        Set the bids for the order book.
        """
        self.bids = bids

    def set_order_book(self, asks: dict, bids: dict):
        """
        Set the asks and bids for the order book.
        """
        self.asks = asks
        self.bids = bids

    def write(self, file_name=pair.__str__() + str(int(time.time())) + ".orderbook", use_compression=True, use_base64=True):
        """
        Write the order book to a file, with compression via zlib and encoding with base64.
        """
        # make order book into a serialable object
        object_dict = { OrderBook: self }
        # convert to JSON string
        json_object = jsons.dumps(object_dict, skipkeys=True)
        # conver to bytes
        json_bytes = json_object.encode('utf-8')

        ret_object = json_bytes
        # compress JSON string via zlib
        if (use_compression & use_base64): 
            # compress JSON string via zlib
            ret_object = zlib.compress(json_bytes)
            # encode compressed JSON string via base64
            ret_object = base64.b64encode(ret_object).decode('utf-8')
            # append the string to the file
            with open(file_name, "a") as file:
                file.write(ret_object)
                file.write('\n')

        elif (use_compression):
            # compress JSON string via zlib
            ret_object = zlib.compress(json_bytes)
            # append compressed JSON string to file
            with open(file_name, 'wb') as file:
                file.write(ret_object)
                file.write(b'\n')

        elif (use_base64):
            # encode JSON string with base64
            ret_object = base64.b64encode(json_bytes).decode('utf-8')
            # append encoded JSON string to file
            with open(file_name, 'w') as file:
                file.write(ret_object)
                file.write('\n')

        return ret_object