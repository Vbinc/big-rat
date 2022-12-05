from enum import Enum

class Direction(Enum):
    """
    Direction enum, is used to define the direction of the trade.
    - LONG: means that the trade is a betting on the price going up.
    - SHORT: means that the trade is a betting on the price going down.
    """
    LONG = 1
    SHORT = 2
    