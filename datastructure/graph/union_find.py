"""
Wikipedia(https://en.wikipedia.org/wiki/Disjoint-set_data_structure):
  In computer science, a disjoint-set data structure (also called a union–find data structure or merge–find set) is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

This is implementation of data structures union find based on the Princeton lecture: (https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
"""
# here we can abstract type of each node to be ADT, but for the sake of simplicity, we will assume that each node is integer.


class QuickFind:
    """
  Quick Find Union Find:
  - Quick find root of each node: O(1)
  - Slow on unioning between two disjointed set (have to update every single union root of p, and update to q
  if we do the operation union(p,q))
  >>> q = QuickFind(10)
  >>> q.union(2,3)
  >>> q.union(1,4)
  >>> q.union(2,6)
  >>> q.union(7,8)
  >>> q.union(1,9)
  >>> q.union(2,7)
  >>> q.union(8,9)
  >>> q.union(3,4)
  >>> q.find(1,2)
  True
  >>> q.find(3,4)
  True
  >>> q.find(8,9)
  True
  >>> q.find(4,5)
  False
  >>> q.find(2,9)
  True
  """

    def __init__(self, N: int) -> None:
        self.root_ids = [
            i for i in range(N)
        ]  # initialize each node with its id => N disjointed sets initially

    # find if p and q are unified
    def find(self, p: int, q: int) -> bool:
        return self.root_ids[p] == self.root_ids[q]

    def union(self, p: int, q: int) -> None:
        p_root_id = self.root_ids[p]
        # step through each root_id of each node and update to q if the node share the same root_id with p
        for node_id, node_root in enumerate(self.root_ids):
            if node_root == p_root_id:
                self.root_ids[node_id] = self.root_ids[q]


class QuickUnion:
    """
  QuickUnion support:
  - Time complexity for finding root node: O(depth_of_tree) since we have to bubble up until we hit the root node
  - Time complexity to union two root node: O(1) given the references of the two node already
  - Time complexity to find if two node is unified: O(depth_of_tree)
  >>> q = QuickUnion(10)
  >>> q.union(2,3)
  >>> q.union(1,4)
  >>> q.union(2,6)
  >>> q.union(7,8)
  >>> q.union(1,9)
  >>> q.union(2,7)
  >>> q.union(8,9)
  >>> q.union(3,4)
  >>> q.find(1,2)
  True
  >>> q.find(3,4)
  True
  >>> q.find(8,9)
  True
  >>> q.find(4,5)
  False
  >>> q.find(2,9)
  True
  """

    def __init__(self, N: int) -> None:
        self.root_ids = [
            i for i in range(N)
        ]  # initialize each node with its id => N disjointed sets initially

    def root(self, i: int) -> int:
        while i != self.root_ids[i]:
            i = self.root_ids[i]
        return i

    # find if p and q are unified
    def find(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        # set root of p to be the root of q
        self.root_ids[self.root(p)] = self.root(q)


class QuickUnionFirstImprovement:
    """
  QuickUnionSecondImprovement will update it's parent node on the way traversing to find the root node, which result
  if much faster O(logN) if N is the number of nodes
  - Time complexity for finding root node: O(depth_of_tree), maybe a little bit better than the above version a bit
  - Time complexity to union two root node: O(1) given the references of the two node already
  >>> q = QuickUnionFirstImprovement(10)
  >>> q.union(2,3)
  >>> q.union(1,4)
  >>> q.union(2,6)
  >>> q.union(7,8)
  >>> q.union(1,9)
  >>> q.union(2,7)
  >>> q.union(8,9)
  >>> q.union(3,4)
  >>> q.find(1,2)
  True
  >>> q.find(3,4)
  True
  >>> q.find(8,9)
  True
  >>> q.find(4,5)
  False
  >>> q.find(2,9)
  True
  """

    def __init__(self, N: int) -> None:
        self.root_ids = [
            i for i in range(N)
        ]  # initialize each node with its id => N disjointed sets initially
        self.sz = [1] * N

    def root(self, i: int) -> int:
        while i != self.root_ids[i]:
            i = self.root_ids[i]
        return i

    # find if p and q are unified
    def find(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        # set root of p to be the root of q
        root_p, root_q = self.root(p), self.root(q)
        if self.sz[root_p] <= self.sz[root_q]:
            self.sz[root_q] += self.sz[root_p]
            self.root_ids[root_p] = root_q
        else:
            self.sz[root_p] += self.sz[root_q]
            self.root_ids[root_q] = root_p


class QuickUnionSecondImprovement:
    """
  QuickUnionSecondImprovement will keep track of the weight of each union, and make optimized decision of unifying between two node. This method has an other name: PathCompression 
  - Time complexity for finding root node: O(logN), maybe a little bit better than the above version a bit
  - Time complexity to union two root node: O(1) given the references of the two node already
  >>> q = QuickUnionSecondImprovement(10)
  >>> q.union(2,3)
  >>> q.union(1,4)
  >>> q.union(2,6)
  >>> q.union(7,8)
  >>> q.union(1,9)
  >>> q.union(2,7)
  >>> q.union(8,9)
  >>> q.union(3,4)
  >>> q.find(1,2)
  True
  >>> q.find(3,4)
  True
  >>> q.find(8,9)
  True
  >>> q.find(4,5)
  False
  >>> q.find(2,9)
  True
  """

    def __init__(self, N: int) -> None:
        self.root_ids = [
            i for i in range(N)
        ]  # initialize each node with its id => N disjointed sets initially
        self.sz = [1 for _ in range(N)]

    def root(self, i: int) -> int:
        while i != self.root_ids[i]:
            self.root_ids[i] = self.root_ids[self.root_ids[i]]
            i = self.root_ids[i]
        return i

    # find if p and q are unified
    def find(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        # set root of p to be the root of q
        root_p, root_q = self.root(p), self.root(q)
        if self.sz[root_p] <= self.sz[root_q]:
            self.sz[root_q] += self.sz[root_p]
            self.root_ids[root_p] = root_q
        else:
            self.sz[root_p] += self.sz[root_q]
            self.root_ids[root_q] = root_p
