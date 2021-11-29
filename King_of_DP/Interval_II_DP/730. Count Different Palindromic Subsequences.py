class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        memo = {}
        mod = 10 ** 9 + 7
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 零个长度
        if i > j:
            return 0
            # 一个长度
        if i == j:
            return 1

        mod = 10 ** 9 + 7

        # 找出最左右边的index，比较是否有重复的value k
        # 如果 只有一个char，index相等，则 res + 1
        # 如果 有重复的char，针对char 则有三种情况 a + aa + a[xxxx]a = a[xxxx]a + 2 , a[xxxx]a -->取决于中间[xxxx]的个数
        # 即 如果有重复的char，每一层表示 以char为结尾的palindro subsequences个数
        res = 0
        for k in set(s[i:j + 1]):
            left = s.find(k, i, j + 1)
            right = s.rfind(k, i, j + 1)
            if left == right:
                res += 1
            else:
                res += self.dfs(s, left + 1, right - 1, memo) + 2

        memo[(i, j)] = res % mod
        return memo[(i, j)]