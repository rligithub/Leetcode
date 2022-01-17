"""
test
"""


class Solution:
    def minimumCoinFlips(self, coins):
        if not coins:
            return 0

        n = len(coins)
        flip = 0
        cntT = 0

        for i in range(n):
            if coins[i] == 'H':
                flip += 1
            else:
                cntT += 1

            flip = min(flip, cntT)
        return flip



a = Solution()
coins = 'TTTTT'

print(a.minimumCoinFlips(coins))