"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        return self.dfs(root, leaf, None)

    def dfs(self, root, node, prev):
        # 断开旧parent，连接新parent指针
        parent = node.parent
        node.parent = prev

        # 断开left/right指针
        if node.left == prev:
            node.left = None
        if node.right == prev:
            node.right = None

        # 停止条件
        if node == root:
            return node

        # 连接右孩子
        if node.left:
            node.right = node.left
        # 连接左孩子
        node.left = self.dfs(root, parent, node)

        return node