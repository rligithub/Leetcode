class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # flip one zero to get longest consectives Ones
        memo = {}
        return self.dfs(nums, True, 0, 0, memo)

    def dfs(self, nums, flip, pos, cnt, memo):
        if (flip, pos, cnt) in memo:
            return memo[(flip, pos, cnt)]

        if pos == len(nums):
            return cnt

        if nums[pos] == 1:
            return self.dfs(nums, flip, pos + 1, cnt + 1, memo)

        else:
            if not flip:
                return cnt
            else:
                do = self.dfs(nums, False, pos + 1, cnt + 1, memo)
                not_do = self.dfs(nums, flip, pos + 1, 0, memo)
                memo[(flip, pos, cnt)] = max(not_do, do)
                return memo[(flip, pos, cnt)]

