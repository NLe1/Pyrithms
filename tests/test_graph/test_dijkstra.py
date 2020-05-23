from algorithms.graph.shortest_path_undirected_dijkstra import (
    shortest_path_undirected_dijkstra,
)
from datastructure.graph.undirected_graph_node import UndirectedGraphNode
from typing import List, Dict
import random
import unittest
import string
import time
from collections import deque


def get_random_word() -> str:
    return "".join(
        [random.choice(string.ascii_letters + string.digits) for _ in range(10)]
    )


def generate_random_vertex(num_vertices: int) -> List:
    # generate random vertices
    wordList = list(set([get_random_word() for _ in range(num_vertices)]))
    return [UndirectedGraphNode(word) for word in wordList]


def generate_random_edges(vertices: List) -> None:
    numVertices = len(vertices)
    # generate random edges with random cost
    for _ in range(2 * numVertices):
        first_index, second_index = (
            random.randint(0, numVertices - 1),
            random.randint(0, numVertices - 1),
        )
        if first_index != second_index:
            first_vertex, second_vertex = vertices[first_index], vertices[second_index]
            random_weight = random.randint(0, 100)
            if second_vertex not in first_vertex.edges:
                first_vertex.edges[second_vertex] = random_weight
                second_vertex.edges[first_vertex] = random_weight


def generate_graph(num_vertices: int = 100) -> List:
    graph = generate_random_vertex(num_vertices)
    generate_random_edges(graph)
    return graph


def brute_force_get_shortest_path(
    graph: List, start_vertex: UndirectedGraphNode, end_vertex: UndirectedGraphNode
) -> int:
    # brute force finding the minimum path by in BFS and keep track of the current cost for each visited node
    # Time Complexity: O(V * E) because we have to traverse through all the edges of each unvisited vertex in worst case
    # Space Complexity: O(V) because we have to keep track of the visited vertex

    min_cost = float("inf")
    visited = set()

    def dfs(current_vertex, current_cost):
        nonlocal visited, min_cost
        if current_vertex.val == end_vertex.val:
            min_cost = min(min_cost, current_cost)
            return
        # marked the current_vertex already visited
        visited.add(current_vertex)
        for neighbor, neighbor_cost in current_vertex.edges.items():
            if neighbor not in visited:
                dfs(neighbor, neighbor_cost + current_cost)
        # unmarked the current_vertex
        visited.remove(current_vertex)

    dfs(start_vertex, 0)  # lazy dfs
    return min_cost


class TestDijkstra(unittest.TestCase):
    # setting up and tear down
    def setUp(self):
        print(f"Running Test Suite: {self.__class__.__name__}")
        self.start = time.time()

    def tearDown(self):
        print("Operation timing: {:06.5f} seconds".format(time.time() - self.start))

    # actual testcases
    def test_shortest_path_undirected_dijkstra(self):
        # generate 10 tests
        for _ in range(10):
            # create a graph with 20 vertices and 40 edges
            test_graph = generate_graph(20)
            # print_graph(test_graph)
            start_vertex, end_vertex = test_graph[0], test_graph[-1]
            corrected_result = brute_force_get_shortest_path(
                test_graph, start_vertex, end_vertex
            )
            self.assertEqual(
                corrected_result,
                shortest_path_undirected_dijkstra(test_graph, start_vertex, end_vertex),
            )
