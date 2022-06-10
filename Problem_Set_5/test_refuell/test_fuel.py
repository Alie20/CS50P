from fuel import gauge ,convert
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_convert():
    assert convert("3/4")   == 75   and gauge(75) =="75%"
    assert convert("1/2")   == 50   and gauge(50) =="50%"
    assert convert("1/4")   == 25   and gauge(25) =="25%"
    assert convert("99/100")   == 99   and gauge(99) =="F"

    assert convert("4/4")   == 100  and gauge(100) =="F"

    assert convert("1/100") == 1    and gauge(1)=="E"







