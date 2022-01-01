# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # ONE DFS --> TLE
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        return self.dfs(root1, root2, target)

    def dfs(self, root1, root2, target):
        if not root1 or not root2:  # 必须是一个从root1中选，一个从root2中选，只要一个没有，return False
            return False

        if root1.val + root2.val < target:
            return self.dfs(root1.right, root2, target) or self.dfs(root1, root2.right, target)
        if root1.val + root2.val > target:
            return self.dfs(root1.left, root2, target) or self.dfs(root1, root2.left, target)
        else:
            return True


class Solution2:  # TWO DFS --> find target value in root2
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        mid = self.dfs(root2, target - root1.val)
        left = self.twoSumBSTs(root1.left, root2, target)
        right = self.twoSumBSTs(root1.right, root2, target)
        return mid or left or right

    def dfs(self, root, target):
        if not root:
            return False

        if root.val == target:
            return True
        elif target < root.val:
            return self.dfs(root.left, target)
        else:
            return self.dfs(root.right, target)

