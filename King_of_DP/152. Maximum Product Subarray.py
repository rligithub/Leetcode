class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 求最大乘积
        # 正正得正， 负负得正 -- > maintain two dp

        n = len(nums)

        maxdp = [0] * n
        mindp = [0] * n

        maxdp[0] = mindp[0] = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                maxdp[i] = max(maxdp[i - 1] * nums[i], nums[i])
                mindp[i] = min(mindp[i - 1] * nums[i], nums[i])
            else:
                maxdp[i] = max(mindp[i - 1] * nums[i], nums[i])
                mindp[i] = min(maxdp[i - 1] * nums[i], nums[i])

        return max(maxdp)

