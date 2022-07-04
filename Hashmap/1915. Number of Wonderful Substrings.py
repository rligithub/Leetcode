class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        masks = [0]

        for i in range(10):
            masks.append(1 << i)

        table = collections.Counter()
        table[0] = 1

        cur_mask = 0
        res = 0
        for i, ch in enumerate(word):
            cur_mask = cur_mask ^ (1 << (ord(ch) - ord('a')))
            for m in masks:
                res += table[(cur_mask ^ m)]

            table[cur_mask] += 1

        return res