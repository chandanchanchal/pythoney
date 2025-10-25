from dataclasses import dataclass, field, replace
from typing import List, Optional

@dataclass(slots=True, order=True)
class Product:
    id: int
    name: str
    price: float = 0.0
    tags: Optional[list[str]] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

    def discount(self, percent: float) -> "Product":
        new_price = self.price * (1 - percent/100.0)
        return replace(self, price=new_price)

@dataclass(frozen=True)
class FrozenProduct:
    id: int
    name: str
    price: float = 0.0

def main():
    p = Product(1, "Mouse", 499.0)
    print(p)
    p2 = p.discount(10)
    print(p2)

    fp = FrozenProduct(2, "Keyboard", 999.0)
    try:
        fp.price = 10
    except Exception as e:
        print("Mutation failed as expected:", type(e).__name__)

if __name__ == "__main__":
    main()
