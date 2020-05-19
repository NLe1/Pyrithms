"""
Import modules below
from {dir}/{folder} import {filename}
"""
from typing import Dict, List
from collections import deque
from .undirected_graph_node import UndirectedGraphNode


def shortest_path_undirected_dijkstra(
    vertices: List, startNode: UndirectedGraphNode, destNode: UndirectedGraphNode
) -> int:
    """
    Explain algorithms or data structures:

    - Dijkstra algorithm help find the shortest path from any node to other node in the graph(must be weighted but directed or undirected is fine).
    - Dijkstra keep track of the "so-far" shortest path from startNode to the currentNode by having designated list or hash table to keep track of the cost and optimize it each time it investigate the next un-visited graph node.
    """

    visited = set()  # keep track of the visited graph node
    # keep track of the previous node that would yield shortest path at current node
    previous_vertex = {}
    # keep track of the shortest distance from start node to other nodes
    shortest_distance = {key: float("inf") for key in vertices}
    # keep track of the next unvisited node, start with startNode
    unvisited = deque([startNode])

    # The cost of startNode to itself is 0
    shortest_distance[startNode] = 0

    while unvisited:
        currentNode = unvisited.popleft()
        currentCost = shortest_distance[currentNode]
        for neighbor, nextCost in currentNode.edges.items():
            # if this path is better than previous one, update the shortest_distance and previous_vertex
            if currentCost + nextCost < shortest_distance[neighbor]:
                shortest_distance[neighbor] = currentCost + nextCost
                previous_vertex[neighbor] = currentNode

            if neighbor not in visited:
                # add to the unvisited queue
                unvisited.append(neighbor)

        visited.add(currentNode)

    return shortest_distance[destNode]
