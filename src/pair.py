from coin import coin

class trade_pair:
    """
    pair of coins.
    """
    def __init__(self, coin_a: coin, coin_b: coin):
        """
        Create a new pair of coins.
        """
        self.coin_a = coin_a
        self.coin_b = coin_b