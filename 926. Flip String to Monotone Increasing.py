class Solution:
    def minFlipsMonoIncr(self, coins: str) -> int:
        # s = "00110" ----》 00111
        if not coins:
            return 0

        n = len(coins)
        flip = 0
        cnt1 = 0

        for i in range(n):
            if coins[i] == '0':
                flip += 1
            else:
                cnt1 += 1

            flip = min(flip, cnt1)
            print(i, flip, cnt1)
        return flip
