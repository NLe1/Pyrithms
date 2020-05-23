"""
Import modules below
from {dir}/{folder} import {filename}
"""
from typing import Dict, List
from collections import deque
from datastructure.graph.undirected_graph_node import UndirectedGraphNode
from heapq import heapify, heappush, heappop


def shortest_path_undirected_dijkstra(
    vertices: List, start_node: UndirectedGraphNode, dest_node: UndirectedGraphNode
) -> int:
    """
    Explain algorithms or data structures:

    - Dijkstra algorithm help find the shortest path from any node to other node in the graph(must be weighted but directed or undirected is fine).
    - Dijkstra keep track of the "so-far" shortest path from start_node to the currentNode by having designated list or hash table to keep track of the cost and optimize it each time it investigate the next un-visited graph node.
    - This algorithm will use priority queue to optimize the search for the next lowest node that is not yet visited operation => decrease from  O(n^2) to O(n*logn)
    """

    # keep track of the shortest distance from start node to other nodes
    cost = {key: float("inf") for key in vertices}
    cost[start_node] = 0  # update the distance from start_node to itself
    seen = set()  # keep track of the visited node

    def find_next_min_node():
        nonlocal seen, cost
        unvisited_nodes = [
            item for item in cost.items() if item[0] not in seen]
        return min(unvisited_nodes, key=lambda x: x[1])[0] if unvisited_nodes else None

    while True:
        current_min_node = find_next_min_node()
        if not current_min_node:
            break
        node_cost = cost[current_min_node]
        seen.add(current_min_node)
        for neighbor, neighbor_cost in current_min_node.edges.items():
            temp_cost = node_cost + neighbor_cost
            cost[neighbor] = min(temp_cost, cost[neighbor])
    return cost[dest_node]
