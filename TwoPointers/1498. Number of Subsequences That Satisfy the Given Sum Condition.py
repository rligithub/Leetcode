class Solution2:  # two pointers
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        nums.sort()

        res = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1

        return res % mod

