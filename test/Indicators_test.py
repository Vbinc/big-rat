import pytest
from src.Indicators import IndicatorData

# create a test IndicatorData instance
@pytest.fixture
def indicator_data():
    return IndicatorData('test_indicator_data')

def test_init(indicator_data):
    # test that the filename attribute is set correctly
    assert indicator_data.filename == 'test_indicator_data.indicator'

def test_write(indicator_data):
    # test that the write method returns the expected string
    assert indicator_data.write('foo', 0.5, 123456) == 'foo_0.5_123456'

def test_write_to_file(indicator_data):
    # test that the write method writes the expected string to the file
    indicator_data.write('bar', 0.25, 654321)
    with open(indicator_data.filename) as f:
        # read the written line from the file
        written_line_1 = f.readline()
        written_line_2 = f.readline()
    assert written_line_1 == 'foo_0.5_123456\n'
    assert written_line_2 == 'bar_0.25_654321\n'
