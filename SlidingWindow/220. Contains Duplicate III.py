class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 先固定left， 找right --> 判断
        # 每次更新left的话，重设right的值为left + 1
        idxs = sorted(range(len(nums)), key=lambda i: nums[i]) # sort index by num value
        nums = [nums[idx] for idx in idxs]  # sort num value
        print(idxs)
        print(nums)
        left, right = 0, 1  # two pointers
        while right < len(nums):
            if nums[right] - nums[left] <= t:  # diff is always positive
                if abs(idxs[right] - idxs[left]) <= k:
                    return True
                right += 1   # diff could be bigger
            else:
                left += 1  # diff should be smaller
                right = left + 1  # back to the beginning
        return False