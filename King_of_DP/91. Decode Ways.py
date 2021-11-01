class Solution:
    def numDecodings(self, s: str) -> int:
        # decode by two digits or by one digits
        memo = {}
        return self.dfs(s, 0, memo)

    def dfs(self, s, pos, memo):
        if pos in memo:
            return memo[pos]

        # no mapping for zero
        if pos < len(s) and s[pos] == '0':
            return 0

            # out of range
        if pos > len(s):
            return 0

        # decode finished
        if pos == len(s):
            return 1

        one = self.dfs(s, pos + 1, memo)

        two = 0
        if 1 <= int(s[pos:pos + 2]) <= 26:
            two = self.dfs(s, pos + 2, memo)

        memo[pos] = one + two
        return memo[pos]