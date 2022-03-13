class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # combination of n char --> permutation --> print kth path

        path = ''
        res = []

        self.dfs(n, path, res)
        res = sorted(res)
        if k <= len(res):
            return res[k - 1]
        return ''

    def dfs(self, n, path, res):

        if len(path) == n:
            res.append(path)
            return

        for char in ('a', 'b', 'c'):
            if not path or (path and path[-1] != char):
                self.dfs(n, path + char, res)