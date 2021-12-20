# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # use GLOBAL variable
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # BST

        self.maxx = float('inf')
        self.res = None

        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if not root:
            return

        if abs(root.val - target) < self.maxx:
            self.maxx = abs(root.val - target)
            self.res = root.val

        self.dfs(root.left, target)
        self.dfs(root.right, target)


class Solution2:  # NOT use gloabl variable --> dfs find diff
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # BST
        res = self.dfs(root, target) + target

        return int(res)

    def dfs(self, root, target):
        if not root:
            return float("inf")

        diff = root.val - target

        if diff == 0:
            return diff
        elif diff > 0:  # BST --> if diff > 0, need to find smaller root.val
            dif_kid = self.dfs(root.left, target)
        else:
            dif_kid = self.dfs(root.right, target)

        return dif_kid if abs(dif_kid) < abs(diff) else diff


class Solution:  # NOT use gloabl variable --> dfs find diff
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        return self.dfs(root, target, root.val)

    def dfs(self, root, target, closest):
        if not root:
            return closest

        if abs(root.val - target) < abs(closest - target):
            closest = root.val

        if target < root.val:
            return self.dfs(root.left, target, closest)
        else:
            return self.dfs(root.right, target, closest)

