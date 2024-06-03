from fuel import convert, gauge
import pytest


"""
This test and fuel.py assumes the users inputs will be (in some shape or form) between 0 - 100
Negatives and n > 100 is not accounted for
"""


def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"

def test_errors():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("3-4")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        convert("0/0")
