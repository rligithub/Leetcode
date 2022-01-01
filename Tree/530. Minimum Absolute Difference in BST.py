# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # local variable 只能对接上下层
        # PLEASE NOTE that prev num may not be root of left node or right node. So can not be passed by reference
        # prev must be value print before cur_node by in-order traversal --> use global variable

        self.res = float('inf')
        self.prev = root
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        if self.prev != root:
            self.res = min(self.res, abs(self.prev.val - root.val))
            self.prev = root

        self.dfs(root.right)