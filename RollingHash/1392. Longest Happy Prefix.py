class Solution:  # rolling hash
    def longestPrefix(self, s: str) -> str:
        # KMP --> prefix = suffix

        table = self.KMP(s)  # table[i] --> happy prefix count when string is from 0 to index i
        last = table[-1]
        return s[:last]

    def KMP(self, pattern):
        n = len(pattern)
        happyPrefix = [0] * n
        cnt = 0  # how many happy prefix at index i
        i = 1  # 因为pattern[0]对应的happy prefix肯定为0， 所以从index 1 开始比较
        while i < n:
            if pattern[i] == pattern[cnt]:
                cnt += 1
                happyPrefix[i] = cnt
                i += 1
            else:
                if cnt != 0:
                    cnt = happyPrefix[cnt - 1]
                else:
                    happyPrefix[i] = 0
                    i += 1
        return happyPrefix