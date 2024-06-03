from plates import is_valid

"""
    # Must start with 2+ LETTERS
    # Char MIN = 2 | MAX = 6
    # Numbers MUST come at the END, AAA222, X AAA22A
    # First number used CANNOT be 0
    # No punctuation/spaces
"""

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("HelloWorld") == False
    assert is_valid("A") == False

def test_startswith():
    assert is_valid("232323") == False
    assert is_valid("H3110") == False
    assert is_valid("AA3333") == True

def test_numbers():
    assert is_valid("HE11O") == False
    assert is_valid("HE110") == True
    assert is_valid("HAL04") == False
    assert is_valid("HA104") == True

def test_punctuation():
    assert is_valid("Hello.") == False
    assert is_valid(".AA333") == False
