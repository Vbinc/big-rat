import jsons
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

    def __init__(self):
        self.interest: tuple[int, int]
        self.potential: tuple[int, int]
        self.position: tuple[int, int, bool]

    def update_interest(self, start: int = 0, end: int = 0):
        if start == 0:
            start = self.interest[0]
        if end == 0:
            end = self.interest[1]

        self.interest = (start, end)

    def update_potential(self, start: int = 0, end: int = 0):
        if start == 0:
            start = self.potential[0]
        if end == 0:
            end = self.potential[1]

        self.potential = (start, end)

    def update_position(self, start: int = 0, end: int = 0, isLong: bool = True):
        if start == 0:
            start = self.position[0]
        if end == 0:
            end = self.position[1]
        if isLong is None:
            isLong = self.position[2]

        self.position = (start, end, isLong)

    def write(self, filename: str, use_compress: bool = True, use_base64: bool = True) -> Union[str, bytes]:
        """
        Write the tradebook to a file.
        """
        if not filename.endswith('.tradebook'):
            filename += '.tradebook'
        # convert to JSON string
        json_str = jsons.dumps(self, skipkeys=True)
        
        if use_compress:
            json_str = json_str.encode('utf-8')
            # compress the bytes
            json_str = zlib.compress(json_str)
            
        if use_base64:
            if (not isinstance(json_str, bytes)):
                json_str = json_str.encode('utf-8')
            # encode the bytes
            json_str = base64.b64encode(json_str).decode('utf-8')
            
        self.interest = tuple()
        self.potential = tuple()
        self.position = tuple()

        # write the bytes to the file
        with open(filename, 'a' if isinstance(json_str, str) else 'ab') as f:
            f.write(json_str)
            f.write('\n' if isinstance(json_str, str) else b'\n')

        return json_str