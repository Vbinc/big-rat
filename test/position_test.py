from src.position import Position
from src.direction import Direction
import pytest

def test_position_class():
    # Test default values
    position = Position()
    assert position.direction == Direction.LONG
    assert position.start == 0
    assert position.stop == 0
    assert position.start_price == 0
    assert position.stop_price == 0

    # Test setTrade() method
    position.setTrade(direction=Direction.SHORT, start=1590238818, stop=1590248818, start_price=100, stop_price=90)
    assert position.direction == Direction.SHORT
    assert position.start == 1590238818
    assert position.stop == 1590248818
    assert position.start_price == 100
    assert position.stop_price == 90

    # Test json() method
    assert position.json() == '{"direction": "SHORT", "start": 1590238818, "start_price": 100, "stop": 1590248818, "stop_price": 90}'
