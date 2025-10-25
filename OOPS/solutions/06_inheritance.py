class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        return f"Woof! I'm {self.name} the {self.breed}"

class Cat(Animal):
    def __init__(self, name, mood='grumpy'):
        super().__init__(name)
        self.mood = mood
    def speak(self):
        return f"Meow... {self.name} is {self.mood}"

class GuideDog(Dog):
    def speak(self):
        return super().speak() + " (trained guide)"

def main():
    animals = [Dog("Buddy", "Labrador"), Cat("Luna"), GuideDog("Hero", "Golden")]
    for a in animals:
        print(a.speak())

if __name__ == "__main__":
    main()
