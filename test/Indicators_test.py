import pytest
from src.Indicators import IndicatorData

# create a test IndicatorData instance
@pytest.fixture
def indicator_data():
    return IndicatorData('test_indicator_data')

def test_init(indicator_data: IndicatorData):
    # test that the filename attribute is set correctly
    assert indicator_data.filename == 'test_indicator_data.indicator'

def test_write(indicator_data: IndicatorData):
    # test that the write method returns the expected string
    assert indicator_data.write('foo', 0.5, 123456) == 'eJyrVspLzE1VslJQSsvPV9JRUCpLzCkF8Q30TIG8kkywpKGRsYmpWS0AJYMMKA=='

def test_write_to_file(indicator_data: IndicatorData):
    # test that the write method writes the expected string to the file
    assert "eJyrVspLzE1VslJQSkosUtJRUCpLzCkF8Q30jEyB3JJMsKyZqYmxkWEtAC7wDEs=" == indicator_data.write('bar', 0.25, 654321)

def test_write_with_compression(indicator_data: IndicatorData):
    # test that the write method compresses the data when use_compression is set to True
    json_bytes = indicator_data.write('foo', 0.5, 123456, use_compression=False, use_base64=False)
    assert isinstance(json_bytes, str)