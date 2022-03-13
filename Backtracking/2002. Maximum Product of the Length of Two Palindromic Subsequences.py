class Solution1:
    def maxProduct(self, s: str) -> int:
        # 3 cases: 1) add char to S1  2) add char to s2   3) not add char  --> max of 3 cases
        memo = {}
        return self.dfs(s, 0, "", "", memo)

    def dfs(self, s, i, s1, s2, memo):
        if (i, s1, s2) in memo:
            return memo[(i, s1, s2)]
        if i >= len(s):
            if self.isPal(s1) and self.isPal(s2):
                return len(s1) * len(s2)
            else:
                return 0

        not_pick = self.dfs(s, i + 1, s1, s2, memo)
        pick1 = self.dfs(s, i + 1, s1 + s[i], s2, memo)
        pick2 = self.dfs(s, i + 1, s1, s2 + s[i], memo)
        memo[(i, s1, s2)] = max(not_pick, pick1, pick2)
        return memo[(i, s1, s2)]

    def isPal(self, s):
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


class Solution:
    def maxProduct(self, s: str) -> int:

        # save all palindromic subsequences in hashmap --> hashmap --> {s: size}
        hashmap = {}
        n = len(s)
        for i in range(1, 1 << n):
            subsequences = ""
            for j in range(n):
                if i >> j & 1 == 1:
                    subsequences += s[j]
            if subsequences == subsequences[::-1]:
                hashmap[i] = len(subsequences)
        # for loop hashmap to find two palindromic subsequences with maxx size product
        res = 0
        for s1, sz1 in hashmap.items():
            for s2, sz2 in hashmap.items():
                if s1 & s2 == 0:
                    res = max(res, sz1 * sz2)
        return res