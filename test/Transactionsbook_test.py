import zlib
import base64
import jsons

from src.TransactionsBook import Transaction, TransactionValue


def test_Transaction_add_value():
    transaction = Transaction('Binance')
    value = TransactionValue(451, 123.45, 10.5, 1234.56)
    transaction.add_value(value)
    assert transaction.values[0] == value


def test_Transaction_add_values():
    transactionAddValuesTest = Transaction('Binance1')
    values = [
        TransactionValue(1589112025, 123.45, 10.5, 1234.56),
        TransactionValue(1589112055, 234.56, 20.5, 2345.67)
    ]
    transactionAddValuesTest.add_values(values)
    assert transactionAddValuesTest.values[0].time == values[0].time
    assert transactionAddValuesTest.values[1].time == values[1].time


def test_Transaction_write():
    transaction = Transaction('Binance')
    values = [
        TransactionValue(1589112025, 123.45, 10.5, 1234.56),
        TransactionValue(1589112055, 234.56, 20.5, 2345.67)
    ]
    transaction.add_values(values)

    # test writing to file without compression and encoding
    file_name = 'test_file.txt'
    result = transaction.write(file_name=file_name, use_compression=False, use_base64=False)
    with open(file_name, 'r') as f:
        assert f.read() == result

    # test writing to file with compression and encoding
    file_name = 'test_file.txt'
    result = transaction.write(file_name=file_name, use_compression=True, use_base64=True)
    with open(file_name, 'r') as f:
        result = f.read()
    json_string = jsons.dumps(transaction, skipkeys=True).encode('utf-8')
    json_string = zlib.compress(json_string)
    json_string = base64.b64encode(json_string).decode('utf-8')
    assert result == json_string
