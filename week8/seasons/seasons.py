from datetime import date
from sys import exit
import inflect

class AgeInMinutes:

    def __init__(self):
        """Initialize with user's birthday and print age in minutes in words"""

        self.birth_date = self.get_birth_date()
        self.minutes: int = self.age_in_minutes(self.birth_date)
        self.print_worded_age(self.minutes)

    @classmethod
    def get_birth_date(cls):
        """Get user date of birth"""

        birth_date_input = input("Date of Birth: ")
        return cls.validate_birth_date(birth_date_input)

    @staticmethod
    def validate_birth_date(date_input: str):
        """Returns ONLY valid date inputs [YYYY-MM-DD]."""

        try:
            return date.fromisoformat(date_input)
        except ValueError:
            exit("Invalid Date of Birth Input")

    @staticmethod
    def age_in_minutes(birth_date):
        """Calculate users age in minutes from birth date to today (midnight to midnight)"""

        return round((date.today() - birth_date).total_seconds() / 60)

    @staticmethod
    def print_worded_age(age_in_minutes):
        """Convert age in minutes to words and print"""

        p = inflect.engine()
        age_in_words= p.number_to_words(age_in_minutes, andword='').capitalize()
        print(f"{age_in_words} minutes")


def main():
    AgeInMinutes()


if __name__ == "__main__":
    main()

#  Classes are confusing to me atm but ill get there eventually
