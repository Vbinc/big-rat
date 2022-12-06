import jsons
from src.interest import Interest
from src.potential import Potential
from src.position import Position
import zlib
import base64
from typing import Union


class Trade:
    """
    Trade is a class that represents everything related to a trade, such as:
    - potential
    - interest
    - position
    ------------------
    Write .tradebook
    """

    def __init__(self, interest=Interest(), potential=Potential(), position=Position()):
        self.interest = interest
        self.potential = potential
        self.position = position

    def get_interest(self):
        return self.interest

    def get_potential(self):
        return self.potential

    def get_position(self):
        return self.position

    def set_trade(self, interest=Interest(), potential=Potential(), position=Position()):
        self.interest = interest
        self.potential = potential
        self.position = position

    def json(self):
        json = {
            "interest": self.interest.json(),
            "potential": self.potential.json(),
            "position": self.position.json()
        }
        return jsons.dumps(json)

    def write_tradebook(self, filename="tradebook.tradebook", use_compress=True, use_base64=True) -> Union[str, bytes]:
        """
        write_tradebook - writes the tradebook to a file

        Parameters
        ----------
        filename : str
            filename to write to
        compress : bool
            compress the file
        base64 : bool
            encode the file in base64
        """
        # convert the object to a JSON string
        json_str = self.json()

        # compress and/or encode the string as needed
        if use_compress:
            json_str = zlib.compress(json_str.encode("utf-8"))
            if use_base64:
                json_str = base64.b64encode(json_str).decode("utf-8")

        # write the string to the file
        if isinstance(json_str, str):
            with open(filename, "w") as f:
                f.write(json_str)
            return json_str
        elif isinstance(json_str, bytes):
            with open(filename, "wb") as f:
                f.write(json_str)
            return json_str
        
        return ""

    