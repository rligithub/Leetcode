class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all combinations

        res = []
        path = []
        self.dfs(nums, 0, path, res)
        return res

    def dfs(self, nums, pos, path, res):
        print(pos, i)
        res.append(path)
        for i in range(pos, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)