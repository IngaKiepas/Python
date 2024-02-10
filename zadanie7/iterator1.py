#iterator zwracający 0, 1, 0, 1, 0, 1, ...
class Iterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current = 1 - self.current
        return result
