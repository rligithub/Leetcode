class Solution1:  # TLE
    def splitArray(self, nums: List[int], m: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        memo = {}
        return self.dfs(nums, presum, m, 0, memo)

    def dfs(self, nums, presum, m, i, memo):
        if (m, i) in memo:
            return memo[(m, i)]

        if i == len(nums):
            if m == 0:
                return 0
            else:
                return float('inf')

        res = float('inf')
        total = 0
        for j in range(i, len(nums)):
            total = presum[j + 1] - presum[i]
            res = min(res, max(total, self.dfs(nums, presum, m - 1, j + 1, memo)))

        memo[(m, i)] = res
        return memo[(m, i)]

