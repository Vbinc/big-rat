class transaction_value: 
    time = 0
    price = 0
    qty = 0
    quote = 0

    def __init__(self, time, price, qty, quote):
        self.time = time
        self.price = price
        self.qty = qty
        self.quote = quote