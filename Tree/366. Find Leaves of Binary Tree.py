# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # print all leaf nodes --> 剥洋葱， 从外到内
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return -1  # return Null nodes level

        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)

        level = max(left, right) + 1
        if level >= len(res):  # add list for each levels
            res.append([])
        res[level].append(root.val)  # if list exist for the same level, append values

        return level


