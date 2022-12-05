from src.coin import Coin

class TradePair:
    """
    TradePair is a pair of coins. It is used to represent a pair of coins in a trade.
    
    Attributes
    ----------
    coin_a : Coin
        The first coin in the pair.
    coin_b : Coin
        The second coin in the pair.
    """
    
    coin_a: Coin = Coin("BTC", "Bitcoin")
    coin_b: Coin = Coin("USDT", "Tether USD")
    
    def __init__(self, coin_a: Coin, coin_b: Coin) -> None:
        """
        Create a new pair of coins.

        Parameters
        ----------
        coin_a : Coin
            The first coin in the pair.
        coin_b : Coin
            The second coin in the pair.

        Examples
        --------
        >>> pair = TradePair(Coin("BTC", "Bitcoin"), Coin("USDT", "Tether USD"))
        >>> print(pair)
        BTC_USDT
        """
        self.coin_a = coin_a
        self.coin_b = coin_b

    def __str__(self) -> str:
        """
        Return the string representation of the pair of coins.

        Returns
        -------
        str
            The string representation of the pair of coins. 

        Examples
        --------
        >>> pair = TradePair(Coin("BTC", "Bitcoin"), Coin("USDT", "Tether USD"))
        >>> print(pair)
        BTC_USDT
        """
        return self.coin_a.ticker + "_" + self.coin_b.ticker