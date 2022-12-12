# big-rat
#### big-rat is a Python library that provides a set of tools for working with indicators, order books, trades, and transactions. It includes the following modules:

* Indicators.py: A module for storing the data of an indicator in a file.
* Orderbook.py: A module for creating an order book for a pair of coins.
* Tradebook.py: A module for representing a trade.
* TransactionsBook.py: A module for representing a transactions book.

## Installation
To install big-rat, use pip and specify the test PyPI repository:

```bash
pip install -i https://test.pypi.org/simple/ big-rat
```

## Usage
To use the modules in the big-rat library, you can import them in your Python code:

```python
from big-rat.Indicators import IndicatorData
from big-rat.Orderbook import OrderBook
from big-rat.Tradebook import Trade
from big-rat.TransactionsBook import TransactionValue, Transaction
```

## TL;DR:
|Class Name|Description|
|:---------|:----------|
|IndicatorData|	📊 Stores the data of an indicator in a file.|
|OrderBook|	💰 Creates an order book for a pair of coins.|
|Trade|	📈 Represents a trade.|
|TransactionValue|	💱 Represents a transaction value from an exchange.|
|Transaction|	📚 Represents a transactions book from an exchange.|

## TS;WR:
You can then use the classes in these modules to work with indicators, order books, trades, and transactions. Here are some examples:

* How to write Indicators using `big-rat`
```python
from Indicators.py import IndicatorData

# Create an IndicatorData object
indicator_data = IndicatorData('my_indicator.indicator')

# Write the data of an indicator to a file
indicator_data.write('My Indicator', 10.5, 1623231451)

```

* How to write Orderbook using `big-rat`

```python
from Orderbook.py import OrderBook

# Create an OrderBook object
order_book = OrderBook('my_order_book.orderbook', 'BTC/USDT')

# Write the order book to a file
order_book.write('my_order_book.orderbook')
```
* How to write Tradebook using `big-rat`

```python
from Tradebook.py import Trade

# Create a Trade object
trade = Trade((10, 20), (30, 40), (50, 60, True))

# Update the interest, potential, and position of the trade
trade.update_interest(start=100, end=200)
trade.update_potential(start=300, end=400)
trade.update_position(start=500, end=600, isLong=False)

# Write the trade to a file
trade.write('my_trade.tradebook')
```
* How to write Transactions using `big-rat`

```python
from TransactionsBook.py import TransactionValue, Transaction

# Create a TransactionValue object
transaction_value = TransactionValue(1623231451, 10.5, 0.01, 0.15)

# Create a Transaction object
transaction = Transaction('Binance')

# Add the transaction value to the transactions book
transaction.add_value(transaction_value)

# Write the transactions book to a file
transaction.write('my_transactions_book.transactionsbook')

```

## License
big-rat is licensed under the [MIT License](https://opensource.org/licenses/MIT).