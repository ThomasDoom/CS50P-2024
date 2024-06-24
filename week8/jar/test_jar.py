from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-10)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(-10)
    with pytest.raises(ValueError):
        jar.deposit(12)
    with pytest.raises(ValueError):
        jar.deposit(1.5)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(7)
    jar.deposit(5)
    assert jar.size == 10


def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(10)
    jar.withdraw(9)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(4)
    jar.withdraw(1)
    assert jar.size == 0
