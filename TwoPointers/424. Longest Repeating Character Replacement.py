class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # at most includes k other distinct letters, total other letter count == k

        window = collections.defaultdict(int)
        left, right = 0, 0
        maxi, res = 0, 0

        while right < len(s):
            window[s[right]] += 1
            maxi = max(maxi, window[s[right]])
            while right - left + 1 - maxi > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
