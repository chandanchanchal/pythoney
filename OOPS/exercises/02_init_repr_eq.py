"""
Exercise 02 — __init__, __repr__, __eq__

Goals:
- Understand constructor & canonical textual representation
- Implement value-based equality
"""

# TODO: Implement a class `Point2D(x, y)` with:
# - __repr__ that returns e.g.: Point2D(x=2, y=5)
# - __eq__ for value-based equality (x and y both equal)
# - distance_to(other) returning Euclidean distance
#
# Add a simple __post_init__-like check in __init__: ensure x and y are numbers.

import math

def main():
    # p = Point2D(2, 5)
    # q = Point2D(2, 5)
    # r = Point2D(3, 5)
    # print(repr(p))           # Point2D(x=2, y=5)
    # print(p == q, p == r)    # True False
    # print(p.distance_to(r))  # 1.0
    pass

if __name__ == "__main__":
    main()
