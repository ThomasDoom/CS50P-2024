class Jar:
    def __init__(self, capacity=12):
        self.positive_int(capacity, "Capacity")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        self.positive_int(n, "Deposit")
        if self.cookies + n > self._capacity:
            raise ValueError("Too many cookies in the jar!")
        self.cookies += n

    def withdraw(self, n):
        self.positive_int(n, "Withdrawal")
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies in the jar to withdraw!")
        self.cookies -= n

    @staticmethod
    def positive_int(n, transaction: str) -> None:
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f"{transaction} must be a positive integer!")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
