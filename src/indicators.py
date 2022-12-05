import jsons
from src.coin import Coin
from src.pair import TradePair
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
    time_unix = 0                                               # time of the indicator
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


    def write(self, file_name=name + pair.__str__() + ".indicator", use_compression=True, use_base64=True):
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
        # convert to JSON string
        json_object = jsons.dumps(self, skipkeys=True)
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

    def set_value(self, value: float):
        self.value = value

    def set_time_unix(self, time_unix: int):
        self.time_unix = time_unix

    def set_indicator(self, value: float, time_unix=time.time()):
        self.value = value
        self.time_unix = time_unix
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def get_time_unix(self):
        return self.time_unix
