class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # similar to #159 Longest-Substring-with-At-Most-Two-Distinct-Characters

        window = collections.defaultdict(int)
        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1
            right += 1

            while len(window) > k:
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count = max(count, right - left)

        return count

