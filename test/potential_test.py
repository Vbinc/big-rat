from src.potential import Potential
import pytest

def test_potential():
    # create a new Potential object
    p = Potential()

    # check that the default values are set
    assert p.start == 0
    assert p.end == 0

    # set the start and end time
    p.set_start(10)
    p.set_end(20)

    # check that the start and end time are set
    assert p.get_start() == 10
    assert p.get_end() == 20

    # check that the JSON representation is correct
    assert p.json() == '{"end": 20, "start": 10}'
