"""
Exercise 10 — Operator Overloading

Goals:
- Implement __str__, arithmetic and comparison dunders
- Provide total ordering via functools
"""

# TODO:
# Implement `Money(amount, currency)`:
# - __str__: "100.00 INR"
# - __add__ and __sub__: only same currency, else raise CurrencyError
# - Rich comparisons based on amount (==, <), only if same currency
# - Use functools.total_ordering to derive other comparisons
#
# Add a small demo.

from functools import total_ordering

class CurrencyError(Exception): ...
def main():
    # a = Money(100, "INR")
    # b = Money(50, "INR")
    # print(a + b)           # 150.00 INR
    # print(a - b)           # 50.00 INR
    # print(a > b, a == b)   # True False
    pass

if __name__ == "__main__":
    main()
