"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # clone circled graph --> use hashmap to copy node, hashmap copy pointer
        if not node:
            return
        hashmap = {}
        self.dfs(node, hashmap)
        return hashmap[node]

    def dfs(self, node, hashmap):
        if node in hashmap:  # visited --> 这道题是个circle 不是tree
            return hashmap[node]

        hashmap[node] = Node(node.val)

        for nei in node.neighbors:
            hashmap[node].neighbors.append(self.dfs(nei, hashmap))

        return hashmap[node]