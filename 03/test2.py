from math import factorial


class GenFactorial:
    def __init__(self, *args):
        self.start = args[0] if len(args) > 1 else 1
        self.stop = args[1] if len(args) > 1 else args[0]
        self.step = args[2] if len(args) == 3 else 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        self.start += self.step
        return factorial(self.start - self.step)


a = GenFactorial(1, 6, 2)
print(a.start, a.stop, a.step)
for num in a:
    print(num)