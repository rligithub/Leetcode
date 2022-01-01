# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        self.visited = set()
        return self.dfs(root, k)

    def dfs(self, root, k):
        if not root:
            return
        left = self.dfs(root.left, k)
        if root.val in self.visited:
            return True
        target = k - root.val
        self.visited.add(target)
        right = self.dfs(root.right, k)

        return left or right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        self.visited = set()
        return self.dfs(root, k)

    def dfs(self, root, k):
        if not root:
            return

        if root.val in self.visited:
            return True
        target = k - root.val
        self.visited.add(target)

        return self.dfs(root.left, k) or self.dfs(root.right, k)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        self.visited = set()
        return self.dfs(root, k)

    def dfs(self, root, k):
        if not root:
            return
        if self.dfs(root.left, k):
            return True
        if root.val in self.visited:
            return True
        target = k - root.val
        self.visited.add(target)
        if self.dfs(root.right, k):
            return True
