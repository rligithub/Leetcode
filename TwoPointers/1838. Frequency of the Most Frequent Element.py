class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 只需要找到某一段区间内，每个值与该区间内最后一个值相差的总和，不超过目标k的最大值

        nums.sort()
        count = 0
        res = 1
        left, right = 0, 1

        while right < len(nums):
            count += (right - left) * (nums[right] - nums[right - 1])  # 计算区间内每个值，与区间内最后一个值相差的总和

            while count > k:
                count -= nums[right] - nums[left]  # 那么就减去区间内最左侧的值与最后一个值的差距
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res