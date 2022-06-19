from working import convert
import pytest

def test_time_AM():
    assert convert("9:00 AM to 5:00 PM")  == "09:00 to 17:00"
    assert convert("10:00 AM to 8:00 PM") == "10:00 to 20:00"
    assert convert("5:00 AM to 12:00 AM") == "05:00 to 00:00"
    assert convert("11:00 AM to 5:00 PM") == "11:00 to 17:00"
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"

def test_time_PM():
    assert convert("8:00 PM to 5:00 AM")  == "20:00 to 05:00"
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"
    assert convert("5:00 PM to 10:00 PM") == "17:00 to 22:00"

def test_format_value():
    with pytest.raises(ValueError):
        convert("8:00 PM - 5:60 AM")

def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert("8:00 PM - 5:60 AM")

def test_wrong_hours():
    with pytest.raises(ValueError):
        convert("13:00 PM to 17:00 PM")





