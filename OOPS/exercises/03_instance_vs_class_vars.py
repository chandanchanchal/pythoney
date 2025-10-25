"""
Exercise 03 — Instance vs Class Variables

Goals:
- Understand shared state vs per-instance state
- Learn the mutability pitfall on class attributes
"""

# TODO:
# Create a class `Tagger` with:
# - class variable: default_tags = ["python"]
# - __init__(self, name, tags=None): if tags is None, use a COPY of default_tags
# - add(tag): add tag to self.tags
# - info(): return "<name>: [tag1, tag2, ...]"
#
# Prove that modifying one instance's tags does not affect another.
# Hint: use list(self.default_tags) to copy.

def main():
    # t1 = Tagger("A")
    # t2 = Tagger("B")
    # t1.add("oop")
    # print(t1.info())  # A: [python, oop]
    # print(t2.info())  # B: [python]
    pass

if __name__ == "__main__":
    main()
