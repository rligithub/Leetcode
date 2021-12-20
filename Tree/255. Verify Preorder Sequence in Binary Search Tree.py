class Solution2:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # BST --> node.val in in between (min, max)

        self.pos = 0
        return self.dfs(preorder, float('-inf'), float('inf'))

    def dfs(self, preorder, minn, maxx):
        if self.pos >= len(preorder):
            return True

        if preorder[self.pos] < minn or preorder[self.pos] > maxx:
            return False

        value = preorder[self.pos]
        self.pos += 1
        left = self.dfs(preorder, minn, value)
        right = self.dfs(preorder, value, maxx)

        return left or right


class Solution:  # TLE
    def verifyPreorder(self, preorder: List[int]) -> bool:

        return self.dfs(preorder, 0, len(preorder) - 1)

    def dfs(self, preorder, start, end):
        if start >= end:
            return True

        root = preorder[start]
        i = start + 1
        while i <= end and preorder[i] < root:
            i += 1
        for j in range(i, end + 1):
            if preorder[j] <= root:
                return False

        return self.dfs(preorder, start + 1, i - 1) and self.dfs(preorder, i, end)

