class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(nums)
        self.dfs(nums, 0, path, res)
        return res

    def dfs(self, nums, pos, path, res):
        res.append(path)

        visited = set()
        for i in range(pos, len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.dfs(nums, i + 1, path + [nums[i]], res)