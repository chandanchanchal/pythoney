from functools import total_ordering

class CurrencyError(Exception): ...

@total_ordering
class Money:
    def __init__(self, amount, currency):
        self.amount = float(amount)
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def _check(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise CurrencyError("currency mismatch")
        return other

    def __add__(self, other):
        other = self._check(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        other = self._check(other)
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.currency == other.currency and self.amount == other.amount

    def __lt__(self, other):
        other = self._check(other)
        return self.amount < other.amount

def main():
    a = Money(100, "INR")
    b = Money(50, "INR")
    print(a + b)           # 150.00 INR
    print(a - b)           # 50.00 INR
    print(a > b, a == b)   # True False

if __name__ == "__main__":
    main()
