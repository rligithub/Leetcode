class Solution:
    def longestAwesome(self, s: str) -> int:
        table = {0: -1}
        res = 0
        cur = 0
        for j, c in enumerate(s):
            k = 1 << (ord(c) - ord('0'))
            cur = cur ^ k
            for i in range(0, 10):
                a = cur ^ (1 << i)
                if a in table:
                    res = max(res, j - table[a])
            if cur in table:
                res = max(res, j - table[cur])
            else:
                table[cur] = j
        return res
