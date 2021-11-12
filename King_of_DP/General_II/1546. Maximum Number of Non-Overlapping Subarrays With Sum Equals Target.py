class Solution1:  # TLE
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # 分割成subarray 求最多有几个subarry的和为target
        # 跟其他题不一样的地方在于 --> 分成subarray后，有的subarray可能对答案没什么影响（sum != target)
        memo = {}
        return self.dfs(nums, target, 0, memo)

    def dfs(self, nums, target, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(nums):
            return 0

        # pos --> start index of subarry
        # i --> ending index of subarry

        res = 0
        summ = 0
        for i in range(pos, len(nums)):
            summ += nums[i]
            if summ == target:
                res = max(res, self.dfs(nums, target, i + 1, memo) + 1)
            else:
                res = max(res, self.dfs(nums, target, i + 1, memo))

        memo[pos] = res
        return memo[pos]


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # create a presum
        n = len(nums)
        presum = [nums[0]]
        for i in range(1, n):
            presum.append(presum[-1] + nums[i])

        # create a table to store {presum: index}
        table = {0: -1}

        res = 0
        l = -1
        # 类似two sum 做法
        # i --> start index of subarray
        for i in range(n):
            if presum[i] - target in table:
                r = table[presum[i] - target]
                if r >= l:
                    res += 1
                    l = i
            table[presum[i]] = i
        return res






