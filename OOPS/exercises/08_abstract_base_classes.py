"""
Exercise 08 — Abstract Base Classes (ABC)

Goals:
- Define an interface with abc.ABC
- Implement concrete classes
- Optionally register virtual subclasses
"""

# TODO:
# Create abstract base class `Serializer` with abstract methods:
# - dumps(obj) -> str
# - loads(s: str) -> object
#
# Implement:
# - JsonSerializer using json
# - CsvSerializer for list[dict[str, Any]] (comma-separated, header from keys)
#
# Show polymorphic use: given a Serializer, round-trip an object.

from abc import ABC, abstractmethod

def main():
    # j = JsonSerializer()
    # data = {"name": "Alice", "age": 30}
    # s = j.dumps(data); print(s); print(j.loads(s))
    #
    # rows = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    # c = CsvSerializer()
    # csv_text = c.dumps(rows); print(csv_text); print(c.loads(csv_text))
    pass

if __name__ == "__main__":
    main()
