"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        orig_copy = {}

        def helper(node):
            if not node:
                return
            
            if node in orig_copy:
                return orig_copy[node]

            node2 = Node(node.val)
            orig_copy[node] = node2

            for n in node.neighbors:
                node2.neighbors.append(helper(n))
            return node2
        
        return helper(node)