
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 找出不符合要求的node和最closest的root.val --> swap

        self.prev, self.first, self.second = None, None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root

        self.prev = root

        self.dfs(root.right)