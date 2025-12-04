class SimpleRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return SimpleRangeIterator(self.start, self.end)


class SimpleRangeIterator:
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val


if __name__ == "__main__":
    sr = SimpleRange(2, 6)
    for x in sr:
        print(x)
