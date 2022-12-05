class Coin:
    """
    A class to represent a coin with tiker and name.

    Attributes
    ----------
    ticker : str
        The ticker of the coin
    name : str
        The name of the coin
    """
    ticker: str = ""
    name: str = ""
    def __init__(self, ticker: str = "", name: str = "") -> None:
        """
        Create a new coin with the given ticker and name.

        Parameters
        ----------
        ticker : str
            The ticker of the coin
        name : str
            The name of the coin
            
        Examples
        --------
        >>> coin = Coin("BTC", "Bitcoin")
        >>> print(coin)
        >>> BTC
        """
        self.ticker = ticker
        self.name = name
        
    def __str__(self) -> str:
        """
        Return the string representation of the coin.
        
        Returns
        -------
        str
            The string representation of the coin.
            
        Examples
        --------
        >>> coin = Coin("BTC", "Bitcoin")
        >>> print(coin)
        >>> BTC
        """
        return self.ticker
