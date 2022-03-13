class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 打印所有组合使得sum为target，每个数可以用1次, 答案里要去重

        res = []
        path = []
        candidates = sorted(candidates)
        print(candidates)
        self.dfs(candidates, target, 0, 0, path, res)
        return res

    def dfs(self, nums, target, pos, summ, path, res):
        if summ > target:
            return

        if summ == target:
            res.append(path)
            return

        for i in range(pos, len(nums)):
            if i > pos and nums[i - 1] == nums[i]:
                continue
            self.dfs(nums, target, i + 1, summ + nums[i], path + [nums[i]], res)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 打印所有组合使得sum为target，每个数可以用1次, 答案里要去重

        res = []
        path = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, 0, 0, path, res)
        return res

    def dfs(self, nums, target, pos, summ, path, res):
        if summ > target:
            return

        if summ == target:
            res.append(path[:])
            return

        for i in range(pos, len(nums)):
            if i > pos and nums[i - 1] == nums[i]:
                continue
            path.append(nums[i])
            self.dfs(nums, target, i + 1, summ + nums[i], path, res)
            path.pop()