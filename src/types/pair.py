from coin import Coin

class Pair:
    """
    Pair of coins.
    """
    def __init__(self, coin_a: Coin, coin_b: Coin):
        """
        Create a new pair of coins.
        """
        self.coin_a = coin_a
        self.coin_b = coin_b