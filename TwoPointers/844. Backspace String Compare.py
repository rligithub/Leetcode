class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # from right to the left --> checking if two strings are the same after the backspacing

        i, j = len(s) - 1, len(t) - 1
        countS, countT = 0, 0
        while True:
            while i >= 0 and (countS or s[i] == '#'):
                if s[i] == '#':
                    countS += 1
                else:
                    countS -= 1
                i -= 1
            while j >= 0 and (countT or t[j] == '#'):
                if t[j] == '#':
                    countT += 1
                else:
                    countT -= 1
                j -= 1
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1
