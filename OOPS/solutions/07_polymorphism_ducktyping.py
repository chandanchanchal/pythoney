import math

class Square:
    def __init__(self, size):
        self.size = size
    def area(self):
        return self.size * self.size

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

def total_area(shapes):
    total = 0.0
    skipped = 0
    for s in shapes:
        try:
            total += s.area()
        except Exception:
            skipped += 1
    return total, skipped

def main():
    shapes = [Square(2), Circle(1), object(), "bad"]
    print(total_area(shapes))  # (~7.1415..., 2)

if __name__ == "__main__":
    main()
