import time
import jsons


class Interest:
    """
    Interest - is a class that contains start and end, with UNIX timestamp
    and function to write them to file with zlib compression and 
    base64 encoding, compression and encoding are optional
    """

    start: int = 0
    """Start of the interest in UNIX timestamp"""
    end: int = 0
    """End of the interest in UNIX timestamp"""

    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end
        self._time = int(time.time())

    def set_start(self, start: int):
        self.start = start

    def set_end(self, end: int):
        self.end = end

    def get_start(self) -> int:
        return self.start

    def get_end(self) -> int:
        return self.end

    def json(self) -> str:
        """
        write - writes the start and end to file with optional compression and encoding
        """
        # convert to JSON string
        return jsons.dumps(self, skipkeys=True)
