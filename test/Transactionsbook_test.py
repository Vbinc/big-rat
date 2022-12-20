import zlib
import base64
import jsons

from src.TransactionsBook import Transaction, TransactionValue


def test_Transaction_add_value():
    transaction = Transaction('Binance')
    value = TransactionValue(451, 123.45, 10.5, 1234.56, True)
    transaction.add_value(value)
    assert transaction.values[0] == value


def test_Transaction_add_values():
    transactionAddValuesTest = Transaction('Binance1')
    values = [
        TransactionValue(1589112025, 123.45, 10.5, 1234.56, True),
        TransactionValue(1589112055, 234.56, 20.5, 2345.67, False)
    ]
    transactionAddValuesTest.add_values(values)
    assert transactionAddValuesTest.values[0].time == values[0].time
    assert transactionAddValuesTest.values[1].time == values[1].time


def test_Transaction_write():
    transaction = Transaction('Binance')
    values = [
        TransactionValue(1589112025, 123.45, 10.5, 1234.56, True),
        TransactionValue(1589112055, 234.56, 20.5, 2345.67, False)
    ]
    transaction.add_values(values)

    # test writing to file without compression and encoding
    result = transaction.write(file_name="file_name", use_compression=False, use_base64=False)
    assert result == '{"source": "Binance", "values": [{"isBuy": true, "price": 123.45, "qty": 10.5, "quote": 1234.56, "time": 1589112025}, {"isBuy": false, "price": 234.56, "qty": 20.5, "quote": 2345.67, "time": 1589112055}]}'
