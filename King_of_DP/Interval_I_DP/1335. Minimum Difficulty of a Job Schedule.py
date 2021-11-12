class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # 把一堆任务分成几天来做，求最小 sum of (max of job_difficulty at each day)

        # 每天至少一个任务
        if len(jobDifficulty) < d:
            return -1

        memo = {}
        return self.dfs(jobDifficulty, d, 0, memo)

    def dfs(self, nums, d, i, memo):
        if (d, i) in memo:
            return memo[(d, i)]

        n = len(nums)
        if i == n and d == 0:
            return 0

        if i == n or d == 0:
            return float('inf')

        res = float('inf')
        for j in range(i, n):
            maxDiff = max(nums[i:j + 1])
            res = min(res, self.dfs(nums, d - 1, j + 1, memo) + maxDiff)

        memo[(d, i)] = res
        return memo[(d, i)]


