"""
Exercise 06 — Inheritance & super()

Goals:
- Build a base class and specialized subclasses
- Use super() to extend behavior
"""

# TODO: Define classes:
# - Animal(name): speak() -> raise NotImplementedError
# - Dog(name, breed): speak() -> "Woof! I'm <name> the <breed>"
# - Cat(name, mood='grumpy'): speak() -> "Meow... <name> is <mood>"
# - GuideDog(name, breed): subclass of Dog, speak() -> Dog.speak() + " (trained guide)"
#
# Demonstrate polymorphism by iterating a list of animals and calling speak().

def main():
    # animals = [Dog("Buddy", "Labrador"), Cat("Luna"), GuideDog("Hero", "Golden")]
    # for a in animals:
    #     print(a.speak())
    pass

if __name__ == "__main__":
    main()
