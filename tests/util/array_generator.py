import numpy as np


class ArrayGenerator:
    # generate 10 random arrays of random integers with specified size
    def generate(self, lo: int = -10000, hi: int = 10000, size: int = 10000):
        return [np.random.randint(lo, hi, size)]
