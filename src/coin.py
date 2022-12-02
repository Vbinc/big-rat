class coin:
    """
    A class to represent a coin with tiker and name.

    Attributes
    ----------
    ticker : str
        The ticker of the coin
    name : str
        The name of the coin
    """
    ticker = ""
    name = ""
    def __init__(self, ticker, name):
        """
        Create a new coin with the given ticker and name.

        Parameters
        ----------
        ticker : str
            The ticker of the coin
        name : str
            The name of the coin
        """
        self.ticker = ticker
        self.name = name

