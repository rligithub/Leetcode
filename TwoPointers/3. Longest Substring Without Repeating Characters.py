class Solution: # sliding window 
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1
            right += 1
            while window[ch1] > 1:
                ch2 = s[left]
                window[ch2] -= 1
                left += 1

            count = max(count, right - left)
        return count