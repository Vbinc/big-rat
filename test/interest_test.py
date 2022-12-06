import pytest
import time
import jsons

from src.interest import Interest

def test_interest_class():
    # create an instance of the Interest class
    interest = Interest()

    # check that the start and end are set to 0 by default
    assert interest.get_start() == 0
    assert interest.get_end() == 0

    # set the start and end
    interest.set_start(10)
    interest.set_end(20)

    # check that the start and end were set correctly
    assert interest.get_start() == 10
    assert interest.get_end() == 20

    # check that the json method produces the expected JSON string
    assert interest.json() == '{"end": 20, "start": 10}'

    # create another instance of the Interest class
    interest2 = Interest(start=100, end=200)

    # check that the start and end were set correctly
    assert interest2.get_start() == 100
    assert interest2.get_end() == 200

    # check that the json method produces the expected JSON string
    assert interest2.json() == '{"end": 200, "start": 100}'
