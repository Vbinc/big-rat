import pytest
from src.indicators import Indicator

def test_indicator_init():
    """Test the Indicator class initialization"""
    indicator = Indicator("Test Indicator", value=1, time_unix=1)
    assert indicator.name == "Test Indicator"
    assert indicator.value == 1
    assert indicator.time_unix == 1
    
def test_indicator_set_value():
    """Test the Indicator class set_value method"""
    indicator = Indicator("Test Indicator")
    indicator.set_value(1)
    assert indicator.value == 1
    
def test_indicator_set_time_unix():
    """Test the Indicator class set_time_unix method"""
    indicator = Indicator("Test Indicator")
    indicator.set_time_unix(1)
    assert indicator.time_unix == 1
    
def test_indicator_set_indicator():
    """Test the Indicator class set_indicator method"""
    indicator = Indicator("Test Indicator")
    indicator.set_indicator(1, 1)
    assert indicator.value == 1
    assert indicator.time_unix == 1
    
def test_indicator_get_name():
    """Test the Indicator class get_name method"""
    indicator = Indicator("Test Indicator")
    assert indicator.get_name() == "Test Indicator"
    
def test_indicator_get_value():
    """Test the Indicator class get_value method"""
    indicator = Indicator("Test Indicator", value=1)
    assert indicator.get_value() == 1
    
def test_indicator_get_time_unix():
    """Test the Indicator class get_time_unix method"""
    indicator = Indicator("Test Indicator", time_unix=1)
    assert indicator.get_time_unix() == 1
    
def test_indicator_write():
    """Test the Indicator class write method"""
    indicator = Indicator("Test Indicator", value=1, time_unix=1)
    json_indicator = indicator.write("test_indicator_write.txt", use_compression=False, use_base64=False)
    assert json_indicator == """{"name": "Test Indicator", "pair": {"coin_a": {"name": "Bitcoin", "ticker": "BTC"}, "coin_b": {"name": "Tether USD", "ticker": "USDT"}}, "time_unix": 1, "value": 1}"""
    
def test_indicator_write_compressed():
    """Test the Indicator class write method with compression"""
    indicator = Indicator("Test Indicator", value=1, time_unix=1)
    json_indicator = indicator.write("test_indicator_write_compressed.txt", use_compression=True, use_base64=False)
    assert json_indicator == b"x\x9cU\xcb1\x0e\x830\x0c@\xd1\xabD\x9eYX;B\x17f\xd2\x19\xb9\xa9%,J\xa8\x82\xa9\x90\xa2\xdc\x1d'\x12C6\xfb\xf9;\x82\xc7\x95\xe0a\xc0\xd2.f\xf0\x1fv([\x80\xc6\xc0\x0f9\xe8%\x82\xdb\xd8OX\xc6\xbb\xeeX\xb2\xe6L\xd8-\x14\n\xda\x1e\x92J\xe9\xdfUoIf\n\xe65>\xeb\x17\x05\x0b)\x15[i:<\x9f\xca\xad\xee\x7f\xfc\x1e\xf9\xb5M\x177q1\x96"
    
def test_indicator_write_base64():
    """Test the Indicator class write method with base64 encoding"""
    indicator = Indicator("Test Indicator", value=1, time_unix=1)
    json_indicator = indicator.write("test_indicator_write_base64.txt", use_compression=False, use_base64=True)
    assert json_indicator == "eyJuYW1lIjogIlRlc3QgSW5kaWNhdG9yIiwgInBhaXIiOiB7ImNvaW5fYSI6IHsibmFtZSI6ICJCaXRjb2luIiwgInRpY2tlciI6ICJCVEMifSwgImNvaW5fYiI6IHsibmFtZSI6ICJUZXRoZXIgVVNEIiwgInRpY2tlciI6ICJVU0RUIn19LCAidGltZV91bml4IjogMSwgInZhbHVlIjogMX0="
    
def test_indicator_write_compressed_base64():
    """Test the Indicator class write method with compression base64 encoding"""
    indicator = Indicator("Test Indicator", value=1, time_unix=1)
    json_indicator = indicator.write("test_indicator_write_compressed_base64.txt", use_compression=True, use_base64=True)
    assert json_indicator == "eJxVyzEOgzAMQNGrRJ5ZWDtCF2bSGbmpJSxKqIKpkKLcHScSQzb7+TuCx5XgYcDSLmbwH3YoW4DGwA856CWC29hPWMa77liy5kzYLRQK2h6SSunfVW9JZgrmNT7rFwULKRVbaTo8n8qt7n/8Hvm1TRc3cTGW"