from seasons import AgeInMinutes
from datetime import date
import pytest

def test_validate_birth_date():
    valid = "2000-01-01"
    assert AgeInMinutes.validate_birth_date(valid) == date(2000, 1, 1)

    invalid = "2000-13-01"
    with pytest.raises(SystemExit):
        AgeInMinutes.validate_birth_date(invalid)

    invalid_format = "01-01-2000"
    with pytest.raises(SystemExit):
        AgeInMinutes.validate_birth_date(invalid_format)

    empty = ""
    with pytest.raises(SystemExit):
        AgeInMinutes.validate_birth_date(empty)

    non_date = "blah-boo"
    with pytest.raises(SystemExit):
        AgeInMinutes.validate_birth_date(non_date)


if __name__ == "__main__":
    pytest.main()
