class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def scale(self, factor):
        if not isinstance(factor, (int, float)) or factor <= 0:
            raise ValueError("factor must be > 0")
        self.width = self._width * factor
        self.height = self._height * factor

def main():
    r = Rectangle(3, 4)
    print(r.area)  # 12
    r.scale(2)
    print(r.width, r.height, r.area)  # 6 8 48

if __name__ == "__main__":
    main()
