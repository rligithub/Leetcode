class Solution:  # top down dp
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 堆砖块 --> 只能放 长宽高都小等于 下面的砖块 的砖块 在上面， 可以旋转成不同的面，求能堆起来的最高 高度
        # 类似题 --> LIS --> 1301.Number-of-Paths-with-Max-Score （2D LIS）

        # 最短边作为length、中等边作为width、最长边作为height
        nums = sorted(map(sorted, cuboids), reverse=True)

        memo = {}
        return self.dfs(nums, 0, float('inf'), float('inf'), float('inf'), memo)

    def dfs(self, nums, pos, l, w, h, memo):
        if (pos, l, w, h) in memo:
            return memo[(pos, l, w, h)]

        if pos == len(nums):
            return 0

        not_pick = self.dfs(nums, pos + 1, l, w, h, memo)
        pick = 0
        x, y, z = nums[pos]
        # if current cuboid is smaller than prev cuboid, put it on the top
        if x <= l and y <= w and z <= h:
            pick = self.dfs(nums, pos + 1, x, y, z, memo) + z

        memo[(pos, l, w, h)] = max(not_pick, pick)
        return memo[(pos, l, w, h)]

