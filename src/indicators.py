class IndicatorData:
    """
    ### IndicatorData is a class that is used to store the data of an indicator.
    
    ----------
    
    Write `.indicator`
    """
    def __init__(self, filename: str):
        self.filename = filename + '.indicator'

    def write(self, name: str, value: float, time: int):
        with open(self.filename, 'a') as f:
            f.write(f"{name}_{value}_{time}\n")
