class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res = 0
        table = collections.Counter(text)
        count = collections.Counter()
        left = 0
        maxx = 0

        for right in range(len(text)):
            count[text[right]] += 1
            maxx = max(maxx, count[text[right]])
            if right - left + 1 - maxx > 1:
                count[text[left]] -= 1
                left += 1
            res = max(res, min(right - left + 1, table[text[right]]))
        return res