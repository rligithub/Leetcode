class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # bit --> 26 chars

        # step1: save bitmask for each word + save size for each word
        n = len(words)
        masks = [0] * n
        size = [0] * n

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << (ord(ch) - ord("a"))
            masks[i] = bitmask
            size[i] = len(words[i])

        # step2: for loop to find max product of size if mask1 & mask2 == 0
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    res = max(res, size[i] * size[j])
        return res