"""
Exercise 07 — Polymorphism & Duck Typing (EAFP)

Goals:
- Practice polymorphic interfaces without inheritance
- Use EAFP style (try/except) to handle behavior
"""

# TODO:
# Implement a function `total_area(shapes)` that sums `shape.area()` for each.
# Accepts any object that has a callable .area() (duck typing).
# If an object doesn't have area(), skip it and count how many were skipped.
# Return (sum_area, skipped_count).
#
# Provide sample classes: Square(size), Circle(radius) with area().

import math

def main():
    # shapes = [Square(2), Circle(1), object(), "bad"]
    # print(total_area(shapes))  # (~7.1415..., 2)  — 2 skipped
    pass

if __name__ == "__main__":
    main()
