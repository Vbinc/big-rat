"""
Indicator is a class that is used to save the indicator data to file.
"""

import json
import time
import zlib
import base64
from coin import coin
from pair import trade_pair

class indicator:
    """This is class that represents a any Indicator that is a point on a graph
    
    Attributes:
        name (str): The name of the indicator
        value (int): The value of the indicator
        time (int): The UNIX time of the indicator
    """
    name = ""                                                   # name of the indicator
    pair: trade_pair = trade_pair(coin(None, None), coin(None, None))       # pair of the indicator
    value: int = 0                                              # value of the indicator
    time_unix = 0                                               # time of the indicator
    
    def __init__(self, 
            name, 
            pair=trade_pair(
                coin_a=coin("BTC", "Bitcoin"), 
                coin_b=coin("USDT", "Tether USD")), 
            value=0, 
            time_unix=0, 
            save=False):
        """
        Create a new indicator with the given name, value, and time.

        Parameters
        ----------
        name : str
            The name of the indicator
        value : int
            The value of the indicator
        time : int
            The UNIX time of the indicator
        """
        self.name = name
        self.pair = pair
        self.value = value
        self.time_unix = time_unix

        # save the indicator to a file
        if save:
            self.write()


    def write(self, file_name=name + str(int(time.time())) + ".indicator", use_compression=True, use_base64=True):
        """
        Write the indicator to a file, with compression via zlib and encoding with base64.
        """
        # make indicator into a serialable object
        object_dict = { indicator: self }
        # convert to JSON string
        json_object = json.dumps(object_dict, skipkeys=True)
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

    def set_value(self, value):
        self.value = value

    def set_time_unix(self, time_unix):
        self.time_unix = time_unix

    def set_indicator(self, value, time_unix):
        self.value = value
        self.time_unix = time_unix
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def get_time_unix(self):
        return self.time_unix
