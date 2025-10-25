"""
Exercise 09 — Multiple Inheritance & MRO

Goals:
- Understand cooperative super() and the MRO
- Compose mixins to add behavior
"""

# TODO:
# Create mixins:
# - ReprMixin: __repr__ uses class name and __dict__ keys sorted
# - IdMixin: auto-incrementing id per subclass (class-level counter)
#
# Create class Customer(ReprMixin, IdMixin):
# - __init__(name): assign self.id via IdMixin, store name
# - greet(): return f"Customer#{id} {name}"
#
# Print repr(customer) and show MRO with Customer.mro()

def main():
    # c1 = Customer("Ravi")
    # c2 = Customer("Anita")
    # print(c1.greet()); print(c2.greet())
    # print(repr(c1))
    # print(Customer.mro())
    pass

if __name__ == "__main__":
    main()
