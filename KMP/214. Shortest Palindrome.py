class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # abab -->
        prefix = self.getPrefix(s + '#' + s[::-1])  # s+'#'+s[n-1,...,0]的前缀函数
        print(prefix)
        if prefix[-1] == len(s):  # 前缀函数的最后一位即为s的最长回文前缀的长度
            return s
        else:
            return s[prefix[-1]:][::-1] + s

    def getPrefix(self, s):
        n = len(s)
        prefix = [0] * n

        cnt = 0
        i = 1
        while i < n:
            if s[i] == s[cnt]:
                cnt += 1
                prefix[i] = cnt
                i += 1
            else:
                if cnt != 0:
                    cnt = prefix[cnt - 1]
                else:
                    prefix[i] = 0
                    i += 1

        return prefix

