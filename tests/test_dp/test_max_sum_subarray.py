from algorithms.dp.max_sum_subarray import max_sum_subarray
from tests.util.array_generator import ArrayGenerator
from typing import List
import random
import unittest
from itertools import accumulate
import time


def brute_force_find(arr: List) -> int:
    max_sum = float("-inf")
    sum_from_start = list(accumulate(arr))
    for i, cur_sum in enumerate(sum_from_start):
        max_sum = max(max_sum, cur_sum)
        for j in range(i):
            max_sum = max(max_sum, cur_sum - sum_from_start[j])
    return int(max_sum)


class TestDijkstra(unittest.TestCase):
    # setting up and tear down
    def setUp(self):
        print(f"Running Test Suite: {self.__class__.__name__}")
        self.start = time.time()

    def tearDown(self):
        print("Operation timing: {:06.5f} seconds".format(time.time() - self.start))

    # actual testcases
    def test_shortest_path_undirected_dijkstra(self):
        generator = ArrayGenerator()
        easy_test_cases = generator.generate(-100, 100, 100)
        for test_case in easy_test_cases:
            answer = brute_force_find(test_case)
            self.assertEqual(answer, (max_sum_subarray(test_case)))

        hard_test_cases = generator.generate(-10000, 10000, 1000)
        for test_case in hard_test_cases:
            answer = brute_force_find(test_case)
            self.assertEqual(answer, (max_sum_subarray(test_case)))
