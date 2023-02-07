class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy --> max step each

        cur = 0
        for i, num in enumerate(nums):
            if cur < i:
                return False
            cur = max(cur, i + num)

        return cur >= len(nums) - 1