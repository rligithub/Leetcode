class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 给 1 - n 个数，求哪些k个数的组合使得sum为n, 每个数最多用一次

        res = []
        path = []
        self.dfs(1, n, k, 0, path, res)
        return res

    def dfs(self, num, n, k, summ, path, res):

        if k == 0 and summ == n:
            res.append(path)
            return

        for i in range(num, 10):
            self.dfs(i + 1, n, k - 1, summ + i, path + [i], res)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 给 1 - n 个数，求哪些k个数的组合使得sum为n, 每个数最多用一次

        res = []
        path = []
        self.dfs(1, n, k, 0, path, res)
        return res

    def dfs(self, num, n, k, summ, path, res):

        if k == 0 and summ == n:
            res.append(path[:])
            return

        for i in range(num, 10):
            path.append(i)
            self.dfs(i + 1, n, k - 1, summ + i, path, res)
            path.pop()