class Solution1:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # 求给的二进制数组，有几个不同的subsequences，且没有leading zeros
        # no leading zeros --> backward --> get subsequences that ended with num "1"
        # n0 --> # of subsequences ended with "0"
        # n1 --> # of subsequences ended with "1"

        mod = 10 ** 9 + 7
        memo = {}
        r1, r0 = self.dfs(binary, 0, memo)
        return (r1 + ('0' in binary)) % mod

    def dfs(self, s, i, memo):
        if i in memo:
            return memo[i]

        n = len(s)
        if i == n:
            return [0, 0]

        n1, n0 = self.dfs(s, i + 1, memo)
        if s[i] == '0':
            n0 = (n0 + n1) + 1
        else:
            n1 = (n0 + n1) + 1
        memo[i] = [n1, n0]
        return memo[i]


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        mod = 10 ** 9 + 7

        one = 0
        zero = 0
        for i in range(n - 1, -1, -1):
            if binary[i] == '0':
                zero = (one + zero) + 1
            else:
                one = one + zero + 1
        return (one + int('0' in binary)) % mod

s = "1010"
a = Solution()
print(a.numberOfUniqueGoodSubsequences(s))