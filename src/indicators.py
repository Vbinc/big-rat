import os
import sys
import json
import zlib
import base64

# JSON: 
# "$graph-name": {
#   "value": "$point x&y",
#   "time": "$time-UNIX",
# }

class Indicator:
    """This is class that represents a any Indicator that is a point on a graph
    
    Attributes:
        name (str): The name of the indicator
        value (int): The value of the indicator
        time (int): The UNIX time of the indicator
    """
    name = ""
    value = 0
    time = 0
    def __init__(self, name):
        """Make a new indicator with the name of the indicator"""
        self.name = name
        self.value = 0
        self.time = 0
    
    def __init__(self, name, value, time):
        self.name = name
        self.value = value
        self.time = time

    def __init__(self, name, value, time) -> None:
        self.name = name
        self.value = value
        self.time = time

        # write this indicator to the file as a JSON object and compress it via zlib, then convert it to base64
        # if the file doesn't exist, create it
        # if the file does exist, append to it

        self.write()

    def write(self):
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
        with open(self.name, "a") as file:
            file.write(base64_object)
            file.write('\n')


    def set_value(self, value):
        self.value = value

    def set_time(self, time):
        self.time = time

    def set_indicator(self, value, time):
        self.value = value
        self.time = time
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def get_time(self):
        return self.time

    

# test
indicator = Indicator("test", 1, 2)
indicator.set_value(3)
indicator.set_time(4)
indicator.set_indicator(5, 6)
print(indicator.get_name())
print(indicator.get_value())
print(indicator.get_time())
