class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        path = ''
        res = []
        self.dfs(n, k, 0, path, res)
        return res

    def dfs(self, n, k, pos, path, res):

        if pos == n:
            res.append(int(path))
            return

        for i in range(10):
            if not path and i == 0:  # no leading zero
                continue
            if not path or abs(int(path[-1]) - i) == k:
                self.dfs(n, k, pos + 1, path + str(i), res)