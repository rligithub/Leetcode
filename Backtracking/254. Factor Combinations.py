class Solution1:  # TLE
    def getFactors(self, n: int) -> List[List[int]]:
        # 给一个数字n，返回所有组成n乘积的所有组合, factors should be in the range [2, n - 1]

        res = []
        path = []
        self.dfs(2, n, n, path, res)
        return res

    def dfs(self, num, n, product, path, res):

        if product == 1 and len(path) > 1:
            res.append(path)
            return

        for i in range(num, product + 1):
            if product % i != 0:
                continue
            if product // i < 1:
                break
            self.dfs(i, n, product // i, path + [i], res)


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # 给一个数字n，返回所有组成n乘积的所有组合, factors should be in the range [2, n - 1]

        res = []
        path = []
        self.dfs(2, n, n, path, res)
        return res

    def dfs(self, num, n, product, path, res):
        if len(path) > 0:
            res.append(path + [product])

        for i in range(num, int(math.sqrt(product)) + 1):
            if product % i == 0:
                self.dfs(i, n, product // i, path + [i], res)


