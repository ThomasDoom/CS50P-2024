class Jar:
    def __init__(self, capacity=12):
        self._input_check(capacity, "Capacity")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        self._deposit_check(n)
        self._cookies += n

    def withdraw(self, n):
        self._withdraw_check(n)
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

    def _deposit_check(self, n):
        self._input_check(n, "Deposit")
        if self._cookies + n > self._capacity:
            raise ValueError("Cookies are oVERFLOWINGGG!!")

    def _withdraw_check(self, n):
        self._input_check(n, "Withdrawal")
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar!")

    @staticmethod
    def _input_check(n, name):
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"{name} must be a positive integer!")
