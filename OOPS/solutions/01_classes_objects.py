class Stopwatch:
    def __init__(self, name: str, elapsed: int = 0):
        self.name = name
        self.elapsed = int(elapsed)

    def tick(self, seconds: int = 1) -> None:
        if seconds < 0:
            raise ValueError("seconds must be >= 0")
        self.elapsed += int(seconds)

    def reset(self) -> None:
        self.elapsed = 0

    def info(self) -> str:
        return f"Stopwatch(name='{self.name}', elapsed={self.elapsed}s)"

def main():
    sw = Stopwatch("Warmup")
    sw.tick(10)
    sw.tick()
    print(sw.info())  # Stopwatch(name='Warmup', elapsed=11s)
    sw.reset()
    print(sw.info())  # Stopwatch(name='Warmup', elapsed=0s)

if __name__ == "__main__":
    main()
