import math

class Point2D:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def distance_to(self, other: "Point2D") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx*dx + dy*dy) ** 0.5

def main():
    p = Point2D(2, 5)
    q = Point2D(2, 5)
    r = Point2D(3, 5)
    print(repr(p))           # Point2D(x=2, y=5)
    print(p == q, p == r)    # True False
    print(p.distance_to(r))  # 1.0

if __name__ == "__main__":
    main()
