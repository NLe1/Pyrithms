class UndirectedGraphNode:
    """
  Definition of GraphNode
  For the weighted undirected graph:
        A <-> B (cost 4)
        A <-> C (cost 1)
        B <-> C (cost 7)
        B <-> D (cost 2)

  We will have
  [GraphNode {
    val = 'A'
    edges = {
      'B': 4
      'C': 1
    }
  },
  GraphNode {
    val = 'B'
    edges = {
      'A': 4
      'C': 7
      'D': 2
    }
  },
  GraphNode {
    val = 'C'
    edges = {
      'A': 1
      'B': 7
    }
  },
  GraphNode {
    val = 'D'
    edges = {
      'B': 2
    }
  },

  """

    def __init__(self, val: str):
        self.edges : Dict[UndirectedGraphNode, list] = {}
        self.val = val

    def add_edge(self, vertice: str, cost: int):
        self.edges[vertice] = cost
