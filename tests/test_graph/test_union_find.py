from datastructure.graph.union_find import QuickUnionSecondImprovement
from typing import List
import random
import unittest
import time


def find_root(union: QuickUnionSecondImprovement, index: int) -> int:
    root_ids = union.root_ids
    while root_ids[index] != index:
        index = root_ids[index]
    return index


class TestUnionFind(unittest.TestCase):
    ### setting up and tear down
    def setUp(self):
        print(f"Running Test Suite: {self.__class__.__name__}")
        self.start = time.time()

    def tearDown(self):
        print("Operation timing: {:.2f} seconds".format(time.time() - self.start))

    ### test cases
    def test_union_find_complex(self):
        self.test_union_find(100, 1000)

    def test_union_find(self, num_objects: int = 10, num_ops: int = 100):
        # generate 10 tests for num_objects and num_ops union and find operations
        for _ in range(10):
            new_union = QuickUnionSecondImprovement(num_ops)
            start_index, end_index = 0, num_objects - 1

            for _ in range(num_ops):
                index1, index2 = (
                    random.randint(start_index, end_index),
                    random.randint(start_index, end_index),
                )
                while index1 == index2:
                    index1, index2 = (
                        random.randint(start_index, end_index),
                        random.randint(start_index, end_index),
                    )
                new_union.union(index1, index2)
                # test finding
                self.assertEqual(
                    find_root(new_union, index1), find_root(new_union, index2)
                )
