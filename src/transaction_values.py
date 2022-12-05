from src.coin import Coin
from src.pair import TradePair

class TransactionValue: 
    """
    TransactionValue is a class that represents a transaction value from any exchange like binance.
    """
    time: int = 0
    price: float = 0
    qty: float = 0
    quote: float = 0

    def __init__(self, time: int, price: float, qty: float, quote: float) -> None:
        """
        Create a new TransactionValue object.
        
        Parameters
        ----------
        time : int
            The time of the transaction in unix time.
        price : float
            The price of the trade.
        qty : float
            The quantity of the trade.
        quote : float
            The quote of the trade.
        """
        self.time = time
        self.price = price
        self.qty = qty
        self.quote = quote