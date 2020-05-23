from algorithms.sorting import counting_sort, insertion_sort
from tests.util.array_generator import ArrayGenerator
import unittest
import random
from typing import List, Callable, Any
import time


class TestSort(unittest.TestCase):
    # setting up and tear down
    def setUp(self):
        print(f"Running Test Suite: {self.__class__.__name__}")
        self.start = time.time()

    def tearDown(self):
        print("Operation timing: {:06.5f} seconds".format(
            time.time() - self.start))

    def test_counting_sort(self) -> None:
        generator = ArrayGenerator()
        # test easy case
        test_cases = generator.generate(1, 1000, 2000)
        for test_case in test_cases:
            # setting up
            test_case = list(test_case)
            sorted_test_case = list(sorted(test_case))

            # testing
            self.assertEqual(sorted_test_case, counting_sort(test_case))

        # test hard case
        test_cases = generator.generate(-10000, 10000, 50000)
        for test_case in test_cases:
            # setting up
            test_case = list(test_case)
            sorted_test_case = list(sorted(test_case))

            # testing
            self.assertEqual(sorted_test_case, counting_sort(test_case))

    def test_insertion_sort(self) -> None:
        generator = ArrayGenerator()
        easy_test_cases = generator.generate(size=10)
        for test_case in easy_test_cases:
            answer = list(sorted(test_case))
            self.assertEqual(answer, (insertion_sort(test_case)))

        hard_test_cases = generator.generate(size=1000)
        for test_case in hard_test_cases:
            answer = list(sorted(test_case))
            self.assertEqual(answer, insertion_sort(test_case))
