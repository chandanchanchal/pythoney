class PaymentStrategy:
    def pay(self, amount: float) -> None:
        raise NotImplementedError

class UpiPayment(PaymentStrategy):
    def __init__(self, vpa: str):
        self.vpa = vpa
    def pay(self, amount: float) -> None:
        print(f"Paying {amount:.2f} via UPI to {self.vpa}")

class CardPayment(PaymentStrategy):
    def __init__(self, last4: str):
        self.last4 = last4
    def pay(self, amount: float) -> None:
        print(f"Paying {amount:.2f} via Card ****{self.last4}")

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying {amount:.2f} in Cash")

class PaymentFactory:
    @staticmethod
    def create(kind: str, **kwargs) -> PaymentStrategy:
        kind = kind.lower()
        if kind == "upi":
            return UpiPayment(kwargs["vpa"])
        if kind == "card":
            return CardPayment(kwargs["last4"])
        if kind == "cash":
            return CashPayment()
        raise ValueError("Unknown payment kind")

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    def process(self, amount: float) -> None:
        self.strategy.pay(amount)

def main():
    p1 = PaymentProcessor(PaymentFactory.create("upi", vpa="dev@okicici"))
    p2 = PaymentProcessor(PaymentFactory.create("card", last4="1234"))
    p3 = PaymentProcessor(PaymentFactory.create("cash"))
    for p in (p1, p2, p3):
        p.process(250.0)

if __name__ == "__main__":
    main()
