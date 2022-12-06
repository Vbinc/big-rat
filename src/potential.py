import time
import jsons


class Potential:
    """
    Potential - is a class that contains start and and, with UNIX timestamp
    and functions to set and get the values, also function to write them to file
    with zlib compression and base64 encoding, 
    compression and encoding in write function should be optional via parameter
    """

    start: int = 0
    """Start time of potential in UNIX timestamp"""
    end: int = 0
    """End of potential in UNIX timestamp"""

    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def json(self):
        """
        json - returns the object as JSON string
        """
        # convert to JSON string
        return jsons.dumps(self, skipkeys=True)
