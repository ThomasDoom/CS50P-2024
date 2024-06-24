class Jar:
    def __init__(self, capacity=12):
        self._validate_positive_int(capacity, "Capacity")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        self._validate_positive_int(n, "Deposit")
        if self.cookies + n > self._capacity:
            raise ValueError("Too many cookies in the jar!")
        self.cookies += n

    def withdraw(self, n):
        self._validate_positive_int(n, "Withdrawal")
        if n > self.cookies:
            raise ValueError("Not enough cookies in the jar to withdraw!")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

    @staticmethod
    def _validate_positive_int(n, name):
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"{name} must be a positive integer!")
