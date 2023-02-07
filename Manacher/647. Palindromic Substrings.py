class Solution:
    def countSubstrings(self, s: str) -> int:
        # manacher --> 求每个i位置的最长r即有几个palindrome --> 最后全部叠加 sum(p[i])

        t = "@#" + "#".join(list(s)) + "#*"
        n = len(t)
        p = [0] * n

        ctr, maxRight = -1, -1

        for i in range(n):
            if i <= maxRight:
                r = min(p[2 * ctr - i], maxRight - i)
                while i - r > 0 and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1
            else:
                r = 0
                while i - r > 0 and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1
            if i + p[i] > maxRight:
                maxRight = i + p[i]
                ctr = i
                # print(t, p)
        res = 0
        for i in range(n):
            res += (p[i] + 1) // 2
        return res


