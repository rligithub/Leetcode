class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 分割成k份，求subarry average的总和
        # presum
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        memo = {}
        return self.dfs(nums, presum, k, 0, memo)

    def dfs(self, nums, presum, k, i, memo):
        if (k, i) in memo:
            return memo[(k, i)]

        if i == len(nums) and k == 0:
            return 0

        if i == len(nums) or k == 0:
            return float('-inf')

        res = float('-inf')
        for j in range(i, len(nums)):
            average = (presum[j + 1] - presum[i]) / (j + 1 - i)
            # 区间dp，下一步从下一个区间开始
            res = max(res, self.dfs(nums, presum, k - 1, j + 1, memo) + average)

        memo[(k, i)] = res
        return memo[(k, i)]