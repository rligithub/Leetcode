class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # 给一堆房子，要求分配k个信箱，求怎么分配使得每个房子到信箱的距离最短
        # 分配k个信箱 ---> 几个房子share 一个信箱 -- 区间dp
        # 每个房子到信箱的距离最短 --> res += abs(house[i] - average dist)
        houses.sort()
        memo = {}
        return self.dfs(houses, k, 0, memo)

    def dfs(self, nums, k, i, memo):
        if (k, i) in memo:
            return memo[(k, i)]

        n = len(nums)
        if i == n and k == 0:
            return 0

        if i == n or k == 0:
            return float('inf')

        res = float('inf')
        for j in range(i, n):
            # 信箱在的位置 --> 找出这个区间中 最中间的位置 greedy
            average = nums[(i + j) // 2]
            # 每个区间中 每个房子到信箱的距离
            dist = 0
            for num in nums[i:j + 1]:
                dist += abs(num - average)
            res = min(res, self.dfs(nums, k - 1, j + 1, memo) + dist)

        memo[(k, i)] = res
        return memo[(k, i)]





