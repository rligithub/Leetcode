class Solution:  # sliding window O(2n) --> l指针走到尾，并没有回头重新走
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 固定r边界，找最左边界符合条件的位置，从右往左数 subarray 即 r-l+1

        if k == 0:
            return 0

        res = 0
        p = 1
        l = 0
        for r in range(len(nums)):
            p *= nums[right]
            while l <= r and p >= k:
                p //= nums[l]
                l += 1
            res += r - l + 1

        return res