class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # 分割s成subarry 使得 每个subarry组成的数值在1...k中间，问有几种分法
        # 长度不确定 --> k的值有几位 即为 最长长度===> 剪枝
        # 类似题：1959. Minimum Total Space Wasted With K Resizing Operations.py

        memo = {}
        return self.dfs(s, k, 0, memo)

    def dfs(self, s, k, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(s):
            return 1
        mod = 10 ** 9 + 7
        # pos --> start index of subarry
        # i --> ending index of subarry
        res = 0
        for i in range(pos, min(pos + len(str(k)), len(s))):
            if int(s[pos]) != 0 and int(s[pos:i + 1]) <= k:
                res += self.dfs(s, k, i + 1, memo)

        memo[pos] = res % mod
        return memo[pos]

