class Solution1:  # TLE
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # i, j --> index of nums
        # pos --> index of multipliers
        memo = {}
        return self.dfs(nums, multipliers, 0, len(nums) - 1, 0, memo)

    def dfs(self, nums, multipliers, i, j, pos, memo):
        if (i, j, pos) in memo:
            return memo[(i, j, pos)]

        if pos == len(multipliers):
            return 0

        pickleft = nums[i] * multipliers[pos] + self.dfs(nums, multipliers, i + 1, j, pos + 1, memo)
        pickright = nums[j] * multipliers[pos] + self.dfs(nums, multipliers, i, j - 1, pos + 1, memo)

        memo[(i, j, pos)] = max(pickleft, pickright)
        return memo[(i, j, pos)]


class Solution2:  # TLE
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # i, j --> num of nums gets from left, num of nums gets from right
        # i + j == m --> len(multipliers)
        memo = {}
        return self.dfs(nums, multipliers, 0, 0, memo)

    def dfs(self, nums, multipliers, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        n = len(nums)

        if i + j == len(multipliers):
            return 0

        pickleft = nums[i] * multipliers[i + j] + self.dfs(nums, multipliers, i + 1, j, memo)
        pickright = nums[n - 1 - j] * multipliers[i + j] + self.dfs(nums, multipliers, i, j + 1, memo)

        memo[(i, j)] = max(pickleft, pickright)
        return memo[(i, j)]


class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)

        @lru_cache(2000)
        def dp(l, i):
            if i == m: return 0
            pickLeft = dp(l + 1, i + 1) + nums[l] * muls[i]  # Pick the left side
            pickRight = dp(l, i + 1) + nums[n - (i - l) - 1] * muls[i]  # Pick the right side
            return max(pickLeft, pickRight)

        return dp(0, 0)

