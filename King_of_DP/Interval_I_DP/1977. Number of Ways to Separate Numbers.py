class Solution:  # TLE
    def numberOfCombinations(self, num: str) -> int:
        # 加逗号隔开，使得每个数字不是递减的
        # 区间 -- >在哪里隔开  res + 1

        # positve # --> initial prev value = 0
        memo = {}
        return self.dfs(num, 0, '0', memo)

    def dfs(self, num, i, prev, memo):
        if (i, prev) in memo:
            return memo[(i, prev)]

        if i == len(num):
            return 1


        mod = 10 ** 9 + 7

        res = 0
        # 剪枝 --> 后一个的长度 肯定 比prev长度大等，才能大等prev
        for j in range(i + len(prev) - 1, len(num)):
            # if j + 1 - i < len(prev):
            #    continue

            total = num[i:j + 1]
            if num[i] != '0' and int(total) >= int(prev):
                res += self.dfs(num, j + 1, total, memo)

        memo[(i, prev)] = res % mod
        return memo[(i, prev)]

