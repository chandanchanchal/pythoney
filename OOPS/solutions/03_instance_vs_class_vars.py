class Tagger:
    default_tags = ["python"]

    def __init__(self, name, tags=None):
        self.name = name
        self.tags = list(self.default_tags) if tags is None else list(tags)

    def add(self, tag):
        self.tags.append(tag)

    def info(self):
        return f"{self.name}: {self.tags}"

def main():
    t1 = Tagger("A")
    t2 = Tagger("B")
    t1.add("oop")
    print(t1.info())  # A: ['python', 'oop']
    print(t2.info())  # B: ['python']

if __name__ == "__main__":
    main()
