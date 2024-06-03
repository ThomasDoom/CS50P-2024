from bank import value

def test_hello():
    assert value("HELLO!") == 0
    assert value("hello!") == 0
    assert value("Hello, there!") == 0

def test_hey():
    assert value("Hey") == 20
    assert value("hey, boss.") == 20
    assert value("howdy, partner!") == 20

def test_bonjour():
    assert value("Bonjour") == 100
    assert value("What's up?") == 100
    assert value("What do you want...") == 100
