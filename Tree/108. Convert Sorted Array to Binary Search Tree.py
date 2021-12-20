# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # height-balanced ---> root is in middle
        # BST --> left < root.val < right
        if not nums:
            return None

        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, l, r):
        if l > r:
            return None

        mid = (r - l) // 2 + l
        root = TreeNode(nums[mid])

        root.left = self.dfs(nums, l, mid - 1)
        root.right = self.dfs(nums, mid + 1, r)

        return root        