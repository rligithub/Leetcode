class Solution:  # two pointers
    def longestSubstring(self, s: str, k: int) -> int:
        # assume has m distinct letters in the array
        res = 0
        for m in range(1, 27):
            res = max(res, self.twoPointer(s, m, k))

        return res

    def twoPointer(self, s, m, k):
        window = collections.Counter()
        left = right = 0
        # count -> how many distinct chars >= k
        count = 0
        res = 0
        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == k:
                count += 1
            right += 1
            # move left
            while left < right and len(window) > m:
                # we will decrement s[left], in turn decrement count
                if window[s[left]] == k:
                    count -= 1
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            if len(window) == m and count == m:
                res = max(res, right - left)
        return res