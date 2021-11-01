class Solution: # TLE
    def checkRecord(self, n: int) -> int:
        # n --> days
        # return num of way for attendance records of eligible attendance award

        memo = {}
        return self.dfs(n, 0, 0, 0, memo)

    def dfs(self, n, pos, absent, late, memo):
        if (pos, absent, late) in memo:
            return memo[(pos, absent, late)]

        mod = 10 ** 9 + 7

        if pos == n:
            return 1

        if absent == 2:
            return 0

        if late == 3:
            return 0

        p = self.dfs(n, pos + 1, absent, 0, memo)

        a = self.dfs(n, pos + 1, absent + 1, 0, memo)

        l = self.dfs(n, pos + 1, absent, late + 1, memo)

        memo[(pos, absent, late)] = (p + a + l) % mod
        return memo[(pos, absent, late)]


