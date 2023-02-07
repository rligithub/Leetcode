class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # hashmap --> 用hashmap存每个word的pattern --> abc

        p = self.convert2code(pattern)

        res = []
        for word in words:
            code = self.convert2code(word)
            if code == p:
                res.append(word)

        return res

    def convert2code(self, word):
        num = 0
        seen = {}
        code = ""
        for ch in word:
            if ch not in seen:
                num += 1
                seen[ch] = chr(ord('a') + num)
                code += chr(ord('a') + num)
            else:
                code += seen[ch]
        return code