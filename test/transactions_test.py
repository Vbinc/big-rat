from src.transaction_values import TransactionValue
from src.transactions import Transaction
import time
import pytest

def test_transaction():
    transaction1 = Transaction("test")
    assert transaction1.source == "test"
    
def test_transaction2():
    transaction1 = Transaction("test")
    transaction1.add_value(TransactionValue(time=int(time.time()), price=1, qty=1, quote=1))
    
    
