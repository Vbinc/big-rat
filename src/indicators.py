"""
Indicator is a class that is used to save the indicator data to file.
"""

import json
import time
import zlib
import base64
from point import Point
from pair import Pair

class Indicator:
    """This is class that represents a any Indicator that is a point on a graph
    
    Attributes:
        name (str): The name of the indicator
        value (int): The value of the indicator
        time (int): The UNIX time of the indicator
    """
    name = ""               # name of the indicator
    pair: Pair = None       # pair of the indicator
    value: Point = None     # value of the indicator
    time_unix = 0           # time of the indicator
    
    def __init__(self, name, pair=Pair("BTC", "USDT"), value=Point(0, 0), time_unix=0, save=False):
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

        if save:
            self.write()


    def write(self, file_name=name + str(int(time.time())) + ".indicator"):
        """
        Write the indicator to a file, with compression via zlib and encoding with base64.
        """
        # make indicator into a serialable object
        object_dict = { Indicator: self }
        # convert to JSON string
        json_object = json.dumps(object_dict, skipkeys=True)
        # conver to bytes
        json_bytes = json_object.encode('utf-8')
        # compress JSON string via zlib
        compressed_object = zlib.compress(json_bytes)
        # convert to base64
        base64_object = base64.b64encode(compressed_object).decode('utf-8')
        # write to file
        # if the file doesn't exist, create it
        # if the file does exist, append to it

        # file_name is $ticker+$UNIXtime_unix.indicator

        with open(file_name, "a") as file:
            file.write(base64_object)
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

    

# test
indicator = Indicator("test", 1, 2)
indicator.set_value(3)
indicator.set_time_unix(4)
indicator.set_indicator(5, 6)
indicator.write()
print(indicator.get_name())
print(indicator.get_value())
print(indicator.get_time_unix())
