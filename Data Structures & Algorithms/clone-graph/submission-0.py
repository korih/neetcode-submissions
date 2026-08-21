"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old = {}

        def dfs(node):
            # if seen before we just return mapping
            if node in old:
                return old[node]
            
            # create copy
            copy = Node(node.val)
            # map node to copy
            old[node] = copy
            # look through neighbors, recurse on each to create mapping
            # append to mapping to make it match
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None