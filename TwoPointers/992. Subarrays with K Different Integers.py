class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # similar to #340
        return self.findMost(nums, k) - self.findMost(nums, k - 1)

    def findMost(self, s, k):
        window = collections.defaultdict(int)
        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1

            while len(window) > k:
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count += right - left + 1
            right += 1
        return count

