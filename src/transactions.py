from src.transaction_values import TransactionValue
import time
import zlib
import base64
import jsons


class Transaction:
    """
    ### Transaction - is a class that represents a transactions book from any exchange like binance.
    --------
    Methods
    * `add_value` - adds a value to the values list
    * `add_values` - adds a list of values to the values list
    * `write` - writes the values to file with optional compression and encoding
    """
    source: str = ""
    values: list[TransactionValue] = []

    def __init__(self, source) -> None:
        self.source = source

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

    def write(self, file_name: str = source + ".tradebook", use_compression: bool = True, use_base64: bool = True) -> None:
        """
        ### Write the indicator to a file, with compression via zlib and encoding with base64.
        
        #### Parameters
        ----------
        * file_name : `str`
            The name of the file to write to
        
        * use_compression : `bool`
            Whether or not to use zlib compression
            
        * use_base64 : `bool`
            Whether or not to use base64 encoding
        """
        # convert to JSON string bytes
        json_string = jsons.dumps(self, skipkeys=True)

        # compress JSON string via zlib
        if (use_compression & use_base64):
            # compress JSON string via zlib
            ret_object = zlib.compress(json_string.encode('utf-8'))
            # encode compressed JSON string via base64
            ret_object = base64.b64encode(ret_object).decode('utf-8')
            # append the string to the file
            with open(file_name, "a") as file:
                file.write(ret_object)
                file.write('\n')

        elif (use_compression):
            # compress JSON string via zlib
            ret_object = zlib.compress(json_string.encode('utf-8'))
            # append compressed JSON string to file
            with open(file_name, 'wb') as file:
                file.write(ret_object)
                file.write(b'\n')

        elif (use_base64):
            # encode JSON string with base64
            ret_object = base64.b64encode(
                json_string.encode('utf-8')).decode('utf-8')
            # append encoded JSON string to file
            with open(file_name, 'w') as file:
                file.write(ret_object)
                file.write('\n')

        else:
            # append JSON string to file
            with open(file_name, 'w') as file:
                file.write(json_string)
                file.write('\n')
