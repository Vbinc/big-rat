import jsons
from direction import Direction

class Position:
    """
    trade - is a class that represent long/short position, that contains start and and, with UNIX timestamp
    and functions to set and get the values, also function to write them to file
    """
    direction: Direction = Direction.LONG
    start = 0
    stop = 0
    start_price = 0
    stop_price = 0

    def __init__(self, direction=Direction.LONG, start=0, stop=0, start_price=0, stop_price=0):
        self.direction = direction
        self.start = start
        self.stop = stop
        self.start_price = start_price
        self.stop_price = stop_price

    def get_direction(self):
        return self.direction
    
    def get_start(self):
        return self.start

    def get_stop(self):
        return self.stop

    def get_start_price(self):
        return self.start_price

    def get_stop_price(self):
        return self.stop_price

    def setTrade(self, direction: Direction = direction, start=start, stop=stop, start_price=start_price, stop_price=stop_price):
        """
        setTrade - sets the trade values

        Parameters
        ----------
        direction : str
            long or short
        start : str
            start time
        stop : str
            stop time
        start_price : str
            start price
        stop_price : str
            stop price
        """
        self.direction = direction
        self.start = start
        self.stop = stop
        self.start_price = start_price
        self.stop_price = stop_price

    def json(self):
        """
        json - returns the trade as JSON string
        """
        return jsons.dumps(self, skipkeys=True)
