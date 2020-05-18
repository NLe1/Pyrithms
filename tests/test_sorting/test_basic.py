from algorithms.sorting import counting_sort

import numpy as np
import unittest
import random


class ArrayGenerator:
    # generate 10 random arrays with high frequency and low range
    def generate_low_range_high_freq(self):
        return [
            np.random.randint(100, 1000, random.randint(1000, 10000)) for _ in range(10)
        ]


class BasicTestSuite(unittest.TestCase):
    def test_counting_sort(self):
        test_cases = ArrayGenerator().generate_low_range_high_freq()
        for test_case in test_cases:
            # setting up
            test_case = list(test_case)
            sorted_test_case = list(sorted(test_case))

            # testing
            self.assertEqual(sorted_test_case, counting_sort(test_case))
