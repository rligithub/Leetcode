class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = ""
        s = s.split()
        for word in s:
            word = list(word)
            l, r = 0, len(word)-1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            res += "".join(word) + " "
        return res[:n]