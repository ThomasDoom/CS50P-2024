from twttr import shorten

def test_limits():
    assert shorten("AEIOUaeiou") == ""
    assert shorten("") == ""
    assert shorten("!,.:a:.,?") == "!,.::.,?"

def test_main():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("just setting up my twttr") == "jst sttng p my twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_numbers():
    assert shorten("H3ll0, w0r1d") == "H3ll0, w0r1d"
    assert shorten("1e23456789a") == "123456789"
