# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        # path --> root to leaf

        return self.dfs(root, arr, 0)

    def dfs(self, root, arr, pos):
        if not root:
            return False

        if pos == len(arr):
            return False

        if root.val != arr[pos]:
            return False

        if not root.left and not root.right and root.val == arr[len(arr) - 1]:
            return True

        return self.dfs(root.left, arr, pos + 1) or self.dfs(root.right, arr, pos + 1)


class Solution2:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        # path --> root to leaf

        return self.dfs(root, arr, 0)

    def dfs(self, root, arr, pos):
        if not root:
            return False

        if pos == len(arr):
            return False

        if not root.left and not root.right and root.val == arr[len(arr) - 1]:
            return True

        if root.val == arr[pos]:
            return self.dfs(root.left, arr, pos + 1) or self.dfs(root.right, arr, pos + 1)
        else:
            return False
