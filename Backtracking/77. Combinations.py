class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 返回1-n的所有k个数的combination

        res = []
        path = []
        self.dfs(1, n, k, path, res)
        return res

    def dfs(self, num, n, k, path, res):

        if k == 0:
            res.append(path)
            return

        for i in range(num, n + 1):
            self.dfs(i + 1, n, k - 1, path + [i], res)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 返回1-n的所有k个数的combination

        res = []
        path = []
        self.dfs(1, n, k, path, res)
        return res

    def dfs(self, num, n, k, path, res):

        if k == 0:
            res.append(path[:])
            return

        for i in range(num, n + 1):
            path.append(i)
            self.dfs(i + 1, n, k - 1, path, res)
            path.pop()
