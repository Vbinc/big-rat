import jsons
from interest import Interest
from potential import Potential
from position import Position


class Trade:
    """
    Trade is a class that represents everything related to a trade, such as:
    - potential
    - interest
    - position
    ------------------
    Write .tradebook
    """

    interest: Interest = Interest()
    potential: Potential = Potential()
    position: Position = Position()

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

    def write_tradebook(self, filename="tradebook.tradebook", compress=True, base64=True):
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
        if compress:
            import zlib
            if base64:
                import base64
                with open(filename, "w") as f:
                    f.write(base64.b64encode(zlib.compress(self.json().encode("utf-8"))).decode("utf-8"))
            else:
                with open(filename, "wb") as f:
                    f.write(zlib.compress(self.json().encode("utf-8")))
        else:
            with open(filename, "w") as f:
                f.write(self.json())
    