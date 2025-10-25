"""
Exercise 12 — Composition, Strategy & Factory Pattern

Goals:
- Prefer composition over inheritance
- Implement Strategy (pluggable behavior)
- Implement a simple Factory for object creation
"""

# TODO:
# Create a PaymentProcessor that delegates to a strategy:
# - Strategy interface: .pay(amount)
# - Concrete strategies: UpiPayment(vpa), CardPayment(last4), CashPayment()
#
# PaymentFactory.create(kind, **kwargs) -> returns correct strategy
# PaymentProcessor(strategy).process(amount) -> uses strategy.pay(amount)
#
# Demo: build processors via factory and process payments.

def main():
    # p1 = PaymentProcessor(PaymentFactory.create("upi", vpa="dev@okicici"))
    # p2 = PaymentProcessor(PaymentFactory.create("card", last4="1234"))
    # p3 = PaymentProcessor(PaymentFactory.create("cash"))
    # for p in (p1, p2, p3):
    #     p.process(250.0)
    pass

if __name__ == "__main__":
    main()
