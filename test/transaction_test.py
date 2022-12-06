import pytest
import jsons

from src.transaction_values import TransactionValue
from src.transactions import Transaction

# test data
transaction_values = [
    TransactionValue(time=1620000000000, price=1.0, qty=1.0, quote=1.0),
    TransactionValue(time=1620000000001, price=2.0, qty=2.0, quote=4.0),
    TransactionValue(time=1620000000002, price=3.0, qty=3.0, quote=9.0),
]
source = "binance"

@pytest.fixture
def transaction():
    return Transaction(source)

def test_add_value(transaction):
    # add a single transaction value
    transaction.add_value(transaction_values[0])
    assert transaction.values == [transaction_values[0]]

    # add another transaction value
    transaction.add_value(transaction_values[1])
    assert transaction.values == [transaction_values[0], transaction_values[1]]

def test_add_values(transaction):
    # add a list of transaction values
    transaction.add_values(transaction_values)
    assert transaction.values[0].time == transaction_values[0].time
    assert transaction.values[1].time == transaction_values[1].time
    assert transaction.values[2].time == transaction_values[2].time
    
    assert transaction.values[0].price == transaction_values[0].price
    assert transaction.values[1].price == transaction_values[1].price
    assert transaction.values[2].price == transaction_values[2].price
    
    assert transaction.values[0].qty == transaction_values[0].qty
    assert transaction.values[1].qty == transaction_values[1].qty
    assert transaction.values[2].qty == transaction_values[2].qty
    
    assert transaction.values[0].quote == transaction_values[0].quote
    assert transaction.values[1].quote == transaction_values[1].quote
    assert transaction.values[2].quote == transaction_values[2].quote

def test_write(transaction, tmpdir):
    # write the transaction values to a file
    file_name = tmpdir.join("test.tradesbook")
    transaction.add_values(transaction_values)
    ret = transaction.write(file_name, use_compression=False, use_base64=False)

    assert ret == jsons.dumps(transaction)

def test_write_compressed(transaction, tmpdir):
    # write the transaction values to a file with compression
    file_name = tmpdir.join("test.tradesbook")
