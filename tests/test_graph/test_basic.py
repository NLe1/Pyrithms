from algorithms.graph import shortest_path_undirected_dijkstra, UndirectedGraphNode
from typing import List, Dict
import random
import unittest
import string
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


def print_graph(graph: List) -> None:
    print("START OF NEW GRAPH")
    print("_----------------------------_")
    for vertice in graph:
        print(f"Vertice name: {vertice.val}")
        print("Edges: ")
        for edges, cost in vertice.edges.items():
            print(f"${vertice.val} <-> {edges.val} Cost : {cost}")
    print("_----------------------------_")


def brute_force_get_shortest_path(
    graph: List, start_vertex: UndirectedGraphNode, end_vertex: UndirectedGraphNode
) -> int:
    # brute force finding the minimum path by in BFS and keep track of the current cost for each visited node
    # Time Complexity: O(V * E) because we have to traverse through all the edges of each unvisited vertex in worst case
    # Space Complexity: O(V) because we have to keep track of the visited vertex

    min_cost = float("inf")
    visited = set()
    unvisited = deque([(start_vertex, 0)])
    while unvisited:
        current_vertex, current_cost = unvisited.popleft()
        if current_vertex.val == end_vertex.val:
            min_cost = min(min_cost, current_cost)
            continue
        # intentionally not adding end_vertex to the visited
        visited.add(current_vertex)
        for neighbor, nextCost in current_vertex.edges.items():
            if neighbor not in visited:
                unvisited.append((neighbor, current_cost + nextCost))
    return min_cost


class BasicTestSuite(unittest.TestCase):
    def test_shortest_path_undirected_dijkstra(self):
        # generate 10 tests
        for _ in range(10):
            # setting up
            test_graph = generate_graph(6)
            # print_graph(test_graph)
            start_vertex, end_vertex = test_graph[0], test_graph[-1]
            corrected_result = brute_force_get_shortest_path(
                test_graph, start_vertex, end_vertex
            )
            self.assertEqual(
                corrected_result,
                shortest_path_undirected_dijkstra(test_graph, start_vertex, end_vertex),
            )
