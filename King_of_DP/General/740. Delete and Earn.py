import collections


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 怎么删数能得到的累积积分最多？（删nums[i]，自动删掉nums[i] + 1 和nums[i] - 1），得到积分nums[i]
        # 对于 value来说 ---> 就是house robber， 相邻不能抢

        arr = [0] * (max(nums) + 1)
        for num in nums:
            arr[num] += num

        memo = {}
        return self.dfs(arr, 0, memo)

    def dfs(self, arr, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos > len(arr) - 1:
            return 0

        pick = self.dfs(arr, pos + 2, memo) + arr[pos]
        not_pick = self.dfs(arr, pos + 1, memo)

        memo[pos] = max(pick, not_pick)
        return memo[pos]