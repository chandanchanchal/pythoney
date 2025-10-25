"""
Exercise 11 — Dataclasses

Goals:
- Use @dataclass with type hints
- Explore frozen, slots, ordering
"""

# TODO:
# Create dataclass Product:
# - fields: id:int, name:str, price:float=0.0, tags:list[str]|None=None
# - post-init: if tags is None, set to []
# - method: discount(percent) -> return new Product with reduced price
# - dunder: __repr__ auto from dataclass
#
# Then create FrozenProduct with frozen=True and try to mutate (should fail).

from dataclasses import dataclass, field

def main():
    # p = Product(1, "Mouse", 499.0)
    # print(p)
    # p2 = p.discount(10)
    # print(p2)
    #
    # fp = FrozenProduct(2, "Keyboard", 999.0)
    # try:
    #     fp.price = 10
    # except Exception as e:
    #     print("Mutation failed as expected:", type(e).__name__)
    pass

if __name__ == "__main__":
    main()
