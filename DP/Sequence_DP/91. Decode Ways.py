class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        return self.dfs(s, 0, memo)

    def dfs(self, s, pos, memo):
        if pos in memo:
            return memo[pos]

        # No mappings for 0
        if pos < len(s) and s[pos] == '0':
            return 0

        # over range
        if pos > len(s):
            return 0

        # decode finished
        if pos == len(s):
            return 1

        takeone = self.dfs(s, pos + 1, memo)

        taketwo = 0
        if 1 <= int(s[pos:pos + 2]) <= 26:
            taketwo = self.dfs(s, pos + 2, memo)

        memo[pos] = takeone + taketwo

        return memo[pos]


s = "226"
a = Solution()
print(a.numDecodings(s))



