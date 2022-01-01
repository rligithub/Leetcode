# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 去最大binary tree，每次把nums中最大的值作为root，再从左边挑最大作为left root，右边最大作为right root

        return self.dfs(nums, 0, len(nums))

    def dfs(self, nums, i, j):
        if i >= j:
            return None

        maxval = max(nums[i:j])
        idx = nums.index(maxval)
        root = TreeNode(maxval)

        root.left = self.dfs(nums, i, idx)
        root.right = self.dfs(nums, idx + 1, j)

        return root


class Solution1:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums)

    def dfs(self, nums):
        if not nums:
            return

        maxval = max(nums)
        idx = nums.index(maxval)
        root = TreeNode(maxval)

        root.left = self.dfs(nums[:idx])
        root.right = self.dfs(nums[idx + 1:])

        return root