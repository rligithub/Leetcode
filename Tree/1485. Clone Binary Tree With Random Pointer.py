# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution1:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # setup a hashmap to save the Node to NodeCopy
        # for loop to copy Node.left
        # for loop to copy Node.right
        # for loop to copy Node.random
        if not root:
            return
        hashmap = collections.defaultdict()

        self.copy_val(root, hashmap)
        self.copy_pointer(root, hashmap)
        return hashmap[root]

    def copy_val(self, root, hashmap):
        if not root:
            return

        hashmap[root] = NodeCopy(root.val)

        self.copy_val(root.left, hashmap)
        self.copy_val(root.right, hashmap)
        return root

    def copy_pointer(self, root, hashmap):
        if not root:
            return

        if root.left:
            hashmap[root].left = hashmap[root.left]
        if root.right:
            hashmap[root].right = hashmap[root.right]
        if root.random:
            hashmap[root].random = hashmap[root.random]

        self.copy_pointer(root.left, hashmap)
        self.copy_pointer(root.right, hashmap)
        return root


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        hashmap = {}
        self.dfs(root, hashmap)
        return hashmap[root]

    def dfs(self, node, hashmap):
        if not node:
            return node

        if node in hashmap:
            return hashmap[node]

        hashmap[node] = NodeCopy(node.val)

        hashmap[node].left = self.dfs(node.left, hashmap)
        hashmap[node].right = self.dfs(node.right, hashmap)
        hashmap[node].random = self.dfs(node.random, hashmap)

        return hashmap[node]
