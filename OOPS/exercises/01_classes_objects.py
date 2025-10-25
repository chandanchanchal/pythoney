"""
Exercise 01 — Classes & Objects (scaffold)

Goals:
- Define a simple class with attributes and methods
- Create objects and access/modify attributes
- Implement a simple method that uses self state
"""

# TODO: Create a class `Stopwatch` that tracks elapsed seconds.
# Requirements:
# - Attributes: name (str), elapsed (int, default 0)
# - Methods:
#   - tick(seconds=1): increase elapsed by given seconds (must be >= 0)
#   - reset(): set elapsed to 0
#   - info(): return a string like "Stopwatch(name='Warmup', elapsed=30s)"
#
# Add simple validation in tick: raise ValueError if seconds < 0

def main():
    # Expected behavior (after you implement Stopwatch):
    # sw = Stopwatch("Warmup")
    # sw.tick(10)
    # sw.tick()
    # print(sw.info())  # Stopwatch(name='Warmup', elapsed=11s)
    # sw.reset()
    # print(sw.info())  # Stopwatch(name='Warmup', elapsed=0s)
    pass

if __name__ == "__main__":
    main()
