class Solution:O(n*2*2)
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        memo = {}
        return self.dfs(nums, firstLen, secondLen, 0, memo)

    def dfs(self, nums, x, y, i, memo):
        if (x, y, i) in memo:
            return memo[(x, y, i)]

        if i >= len(nums):
            return 0

        if x == 0 and y == 0:
            return 0

        not_pick = self.dfs(nums, x, y, i + 1, memo)
        if x == 0:
            pick = self.dfs(nums, x, 0, i + y, memo) + sum(nums[i:i + y])
            res = max(not_pick, pick)
        elif y == 0:
            pick = self.dfs(nums, 0, y, i + x, memo) + sum(nums[i:i + x])
            res = max(not_pick, pick)
        else:
            pick_x = self.dfs(nums, 0, y, i + x, memo) + sum(nums[i:i + x])
            pick_y = self.dfs(nums, x, 0, i + y, memo) + sum(nums[i:i + y])
            res = max(not_pick, pick_x, pick_y)

        memo[(x, y, i)] = res
        return res

    class Solution:  # sliding window O(n)
        def maxSumTwoNoOverlap(self, nums: List[int], f: int, s: int) -> int:

            # subarry --> presum
            # get max sum of two subarray

            n = len(nums)

            if n < f + s:
                return 0

            preSum = [nums[0]]
            for i in range(1, len(nums)):
                preSum.append(preSum[-1] + nums[i])

            summ = preSum[f + s - 1]
            firstSum = preSum[f - 1]
            secondSum = preSum[s - 1]

            for i in range(f + s, n):
                curSum_s = preSum[i] - preSum[i - s]
                curSum_f = preSum[i] - preSum[i - f]

                firstSum = max(firstSum, preSum[i - s] - preSum[i - s - f])  # max_firstLen_summ
                secondSum = max(secondSum, preSum[i - f] - preSum[i - s - f])

                # max_firstLen_Summ + current_secondLen_summ vs max_secondLen_Summ + current_firstLen_summ
                summ = max(summ, firstSum + curSum_s, secondSum + curSum_f)

            return summ

