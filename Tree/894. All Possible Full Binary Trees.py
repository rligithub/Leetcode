# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # top down dp
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        if n == 1:
            return [TreeNode(0)]

        res = []

        for i in range(1, n, 2):  # 1, 3, 5, 7....
            left = self.dfs(i, memo)
            right = self.dfs(n - i - 1, memo)
            for l in left:
                for r in right:
                    res.append(TreeNode(0, l, r))
        memo[n] = res
        return memo[n]


class Solution:  # bottom up
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]

        dp[1] = [TreeNode(0)]
        for i in range(1, n + 1, 2):
            for j in range(1, i, 2):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        dp[i].append(TreeNode(0, left, right))

        return dp[-1]







