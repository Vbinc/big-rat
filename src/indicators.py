from typing import Union
import jsons
import zlib
import base64

class IndicatorData:
    """
    ### IndicatorData is a class that is used to store the data of an indicator.
    
    ----------
    
    Write `.indicator`
    """
    def __init__(self, filename: str):
        if not filename.endswith('.indicator'):
            self.filename = filename + '.indicator'

    def write(self, name: str, value: float, time: int, use_compression=True, use_base64=True) -> Union[bytes, str]: 
        """
        ### Write the data of an indicator to a file.
        
        ----------
        
        Parameters:
        - name: str
            The name of the indicator.
        - value: float
            The value of the indicator.
        - time: int
            The time of the indicator.
        """
        
        data = jsons.dumps({'name': name, 'value': value, 'time': time})
        
        if use_compression:
            data = zlib.compress(data.encode())
            
        if use_base64:
            data = base64.b64encode(data if isinstance(data, bytes) else data.encode()).decode()
        
        with open(self.filename, 'a' if isinstance(data, str) else 'ab') as f:
            f.writelines([data])
            
        return data
