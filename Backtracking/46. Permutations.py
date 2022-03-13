class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, pos, res):
        if pos == len(nums):
            res.append(nums[:])
            return

        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]

            self.dfs(nums, pos + 1, res)
            nums[i], nums[pos] = nums[pos], nums[i]

class Solution:
    def permute(self, nums):

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

class Solution:
    def permute(self, nums):

        res = []
        self.dfs(nums, [], res, set())
        return res

    def dfs(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path)

        for i in range(len(nums)):
            if i in visited: # save index --> make sure not selecting next time
                continue
            visited.add(i)
            self.dfs(nums, path + [nums[i]], res, visited)
            visited.remove(i)


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(nums, res, path)
        return res

    def dfs(self, nums, res, path):
        if len(path) == len(nums):
            res.append(path)
            return
        for num in nums:
            if num not in path:
                self.dfs(nums, res, path + [num])