class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        # 分割成subarray
        # 最多resize k次空间后，求最少浪费空间
        # 类似题 -> 1043. Partition Array for Maximum Sum

        memo = {}
        return self.dfs(nums, k, 0, memo)

    def dfs(self, nums, k, pos, memo):
        if (k, pos) in memo:
            return memo[(k, pos)]

        if pos == len(nums):
            return 0

        if k < 0:
            return float('inf')

        res = float('inf')
        cursize = nums[pos]
        presum = 0
        # pos --> start index of subarry
        # i --> ending index of subarry
        # find a maxpoint in subarry --> so that no need to resize in this subarry
        for i in range(pos, len(nums)):
            cursize = max(cursize, nums[i])
            presum += nums[i]
            cost = cursize * (i - pos + 1) - presum
            res = min(res, self.dfs(nums, k - 1, i + 1, memo) + cost)

        memo[(k, pos)] = res
        return memo[(k, pos)]


