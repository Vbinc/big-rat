import zlib
import base64
import jsons
from typing import Union

class TransactionValue: 
    """
    TransactionValue is a class that represents a transaction value from any exchange like binance.
    """
    time: int = 0
    price: float = 0
    qty: float = 0
    quote: float = 0
    isBuy: bool = True

    def __init__(self, time: int, price: float, qty: float, quote: float, isBuy: bool) -> None:
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
        self.isBuy = isBuy

class Transaction:
    """
    ### Transaction - is a class that represents a transactions book from any exchange like binance.
    --------
    Methods
    * `add_value` - adds a value to the values list
    * `add_values` - adds a list of values to the values list
    * `write` - writes the values to file with optional compression and encoding
    --------
    Write .transactionsbook
    """
    source: str = ""
    values: list[TransactionValue] = []

    def __init__(self, source) -> None:
        self.source = source
        self.values = []

    def add_value(self, value: TransactionValue) -> None:
        self.values.append(value)

    def add_values(self, values: list[TransactionValue]) -> None:
        """
        ### Add a list of trades to values.
        
        ----------
        #### Parameters
        values : `list[TransactionValue]`
            The list of trades to add.
        """
        self.values.extend(values)

    def write(self, file_name: str, use_compression: bool = True, use_base64: bool = True) -> Union[str, bytes]:
        if not file_name.endswith('.transactionsbook'):
            file_name = f"{file_name}.transactionsbook"

        # convert to JSON string bytes
        json_string = jsons.dumps(self, skipkeys=True).encode('utf-8')

        # compress JSON string via zlib
        if use_compression:
            json_string = zlib.compress(json_string)

        # encode JSON string with base64
        if use_base64:
            json_string = base64.b64encode(json_string).decode('utf-8')

        # write the string to the file
        with open(file_name, 'w' if use_base64 else 'wb') as f:
            f.write(json_string)
            f.write('\n' if isinstance(json_string, str) else b'\n')

        self.values = []

        # return the resulting string
        return json_string if isinstance(json_string, str) else json_string.decode('utf-8')

