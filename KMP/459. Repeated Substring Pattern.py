class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # KMP to find happyprefix table
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

        size = n - prefix[-1]
        return n % size == 0 and prefix[-1] != 0