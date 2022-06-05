class Solution1:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i] = Math.max(dp[j], 0) + nums[i] // j 属于 [i - k, i]
        # 维护一个长度不超过 k 的单调递减队列

        n = len(nums)
        dp = [nums[0]] + [0] * (n - 1)  # 处理 base case：i == 0

        queue = collections.deque([0]) # 初始化
        res = nums[0]

        for i in range(1, n):
            # 如果队列长度大于 k + 1 则从队头出列
            while queue and i - queue[0] > k:
                queue.popleft()
            # 根据动态方程式计算当前 dp 的值, 更新当前维护的最大值
            dp[i] = max(dp[queue[0]], 0) + nums[i]
            # maintain max dp[i] in queue[0]，不断从队尾弹出元素
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
            res = max(res, dp[queue[0]])

        return res
