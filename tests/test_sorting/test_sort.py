from algorithms.sorting import counting_sort

import numpy as np
import unittest
import random
from typing import List


class ArrayGenerator:
    # generate 10 random arrays with high frequency and low range
    def generate_low_range_high_freq(self, lo: int, hi:int) -> List:
        return [
            np.random.randint(lo, hi, random.randint(hi, hi * 10)) for _ in range(10)
        ]


class BasicTestSuite(unittest.TestCase):
    def test_counting_sort(self) -> None:
        generator = ArrayGenerator()
        # test easy case
        test_cases = generator.generate_low_range_high_freq(100,1000)
        for test_case in test_cases:
            # setting up
            test_case = list(test_case)
            sorted_test_case = list(sorted(test_case))

            # testing
            self.assertEqual(sorted_test_case, counting_sort(test_case))

        # test hard case
        test_cases = generator.generate_low_range_high_freq(1,10000)
        for test_case in test_cases:
            # setting up
            test_case = list(test_case)
            sorted_test_case = list(sorted(test_case))

            # testing
            self.assertEqual(sorted_test_case, counting_sort(test_case))
        
