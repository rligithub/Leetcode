class Solution1:
    def makesquare(self, matchsticks: List[int]) -> bool:
        maxsumm = sum(matchsticks)
        if len(matchsticks) < 4 or maxsumm % 4 != 0 or max(matchsticks) > (maxsumm / 4):
            return False
        visited = [False] * len(matchsticks)

        return self.dfs(matchsticks, visited, maxsumm / 4, 4, 0, 0)

    def dfs(self, nums, visited, target, k, pos, summ):

        if k == 1:
            return True

        if summ == target:
            return self.dfs(nums, visited, target, k - 1, 0, 0)

        for i in range(pos, len(nums)):
            if visited[i] == False:
                visited[i] = True

                if self.dfs(nums, visited, target, k, i + 1, summ + nums[i]):
                    return True
                visited[i] = False

        return False


class Solution:
    def makesquare(self, nums):
        if not nums:
            return False
        nums = sorted(nums, reverse=True)
        sumn = sum(nums)
        if sumn % 4:
            return False
        return self.dfs(nums, [0, 0, 0, 0], 0, sumn / 4)

    def dfs(self, nums, res, pos, target):
        if pos == len(nums):
            if res[0] == res[1] == res[2]:
                return True
            return False

        for i in range(4):
            if res[i] + nums[pos] > target:
                continue
            res[i] += nums[pos]
            if self.dfs(nums, res, pos + 1, target):
                return True
            res[i] -= nums[pos]

        return False