from typing import Union
from src.coin import Coin
from src.pair import TradePair
import jsons
import time
import zlib
import base64

class Indicator:
    """This is class that represents a any Indicator that is a point on a graph
    
    Attributes:
        * name (str): The name of the indicator
        * value (int): The value of the indicator
        * time (int): The UNIX time of the indicator
        
    Methods:
        * set_value(value): Sets the value of the indicator
        * set_time_unix(time): Sets the UNIX time of the indicator
        * set_indicator(value, time): Sets the value and UNIX time of the indicator
        * get_name(): Returns the name of the indicator
        * get_value(): Returns the value of the indicator
        * get_time_unix(): Returns the UNIX time of the indicator
        * write(file_name, use_compression, use_base64): Writes the indicator to a file
    """
    name = ""                                                   # name of the indicator
    """Name of the indicator"""
    pair: TradePair = TradePair(
        Coin("BTC", "Bitcoin"), 
        Coin("USDT", "Tether USD"))                             # pair of the indicator
    """Pair of the indicator"""
    value: float = 0                                            # value of the indicator
    """Value of the indicator"""
    time_unix: int = 0                                               # time of the indicator
    """Time of the indicator"""
    
    def __init__(self, 
            name, 
            pair=TradePair(
                coin_a=Coin("BTC", "Bitcoin"), 
                coin_b=Coin("USDT", "Tether USD")), 
            value=0, 
            time_unix=0, 
            save=False):
        """
        ### Create a new indicator with the given name, value, and time.

        #### Parameters
        ----------
        * name : str
            The name of the indicator
        * value : int
            The value of the indicator
        * time : int
            The UNIX time of the indicator
        """
        
        self.name = name
        self.pair = pair
        self.value = value
        self.time_unix = time_unix

        # save the indicator to a file
        if save:
            self.write()


    def write(self, file_name=name + ".indicator", use_compression=True, use_base64=True) -> Union[str, bytes]:
        """
        ### Write the indicator to a file, with compression via zlib and encoding with base64.
        ----------
        #### Parameters
        * file_name : str
            The name of the file to write to

        * use_compression : bool
            Whether or not to use zlib compression

        * use_base64 : bool
            Whether or not to use base64 encoding
        """
        # convert to JSON string and encode as bytes
        json_bytes = jsons.dumps(self).encode('utf-8')

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
        else:
            json_bytes = json_bytes.decode('utf-8')

        # write the bytes to the file
        if isinstance(json_bytes, str):
            with open(file_name, "a") as file:
                file.writelines([json_bytes])
        elif isinstance(json_bytes, bytes):
            with open(file_name, "a+b") as file:
                file.writelines([json_bytes])
            print(json_bytes)

        return json_bytes
    
    def set_value(self, value: float):
        self.value = value

    def set_time_unix(self, time_unix: int):
        self.time_unix = time_unix

    def set_indicator(self, value: float, time_unix: int = int(time.time())):
        self.value = value
        self.time_unix = time_unix
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def get_time_unix(self):
        return self.time_unix
