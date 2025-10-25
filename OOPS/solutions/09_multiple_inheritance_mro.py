class ReprMixin:
    def __repr__(self):
        items = ", ".join(f"{k}={getattr(self, k)!r}" for k in sorted(self.__dict__.keys()))
        return f"{self.__class__.__name__}({items})"

class IdMixin:
    _counter = 0
    def __init__(self, *args, **kwargs):
        cls = self.__class__
        if not hasattr(cls, "_counter"):
            cls._counter = 0
        cls._counter += 1
        self.id = cls._counter
        super().__init__(*args, **kwargs)

class Customer(ReprMixin, IdMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def greet(self):
        return f"Customer#{self.id} {self.name}"

def main():
    c1 = Customer("Ravi")
    c2 = Customer("Anita")
    print(c1.greet()); print(c2.greet())
    print(repr(c1))
    print(Customer.mro())

if __name__ == "__main__":
    main()
