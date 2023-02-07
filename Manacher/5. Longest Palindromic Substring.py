class Solution:  # mancher algorithm O(n)
    def longestPalindrome(self, s: str) -> str:
        # """
        #                      MR
        #     {x x x x x x x x x} x x x x
        #             ctr    i

        # """

        # similar to dp ---> p[i] means 以i位置为中心的最长palindro的半径长度
        # 每次更新 crt和maxR 即 已求的最长p[i]对应的位置crt和最右边的位置
        # 检查新的i是否在最右边的位置范围内，是的话--> 可通过中心对称，找出r的起始位置； 否则 --> r起始为0，暴力求r
        # for loop p[i] 找出最长r和位置，打印出来

        t = "#" + "#".join(list(s)) + "#"
        n = len(t)
        p = [0] * n
        ctr = -1
        maxRight = -1

        for i in range(n):
            r = 0
            if i <= maxRight:
                r = min(p[ctr * 2 - i], maxRight - i)
                while 0 < i - r and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1
            else:
                while 0 < i - r and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1

            if i + p[i] > maxRight:  # new i + r
                maxRight = i + p[i]
                ctr = i

        maxSize = -1
        maxIdx = -1
        for i in range(n):
            if maxSize < p[i]:
                maxSize = p[i]
                maxIdx = i

        res = t[maxIdx - maxSize:maxIdx + maxSize + 1]

        return "".join(res.split("#"))
