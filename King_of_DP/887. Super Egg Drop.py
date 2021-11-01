class Solution1:  # TLE
    def superEggDrop(self, k: int, n: int) -> int:
        # 扔鸡蛋，给k个鸡蛋，总共n层楼梯，从x层以上扔下来，会破，x层以下，不会破。求最少要扔几次才能找出x层的位置
        # variable --> k, n
        # res ==> times to try
        # look back 0....i

        memo = {}
        return self.dfs(k, n, memo)

    def dfs(self, k, n, memo):
        if (k, n) in memo:
            return memo[(k, n)]

        # out of range, no egg
        if k == 0:
            return 0

        # base case --> one egg, need to try n times to find
        if k == 1:
            return n

        if n <= 1:
            return n

        res = float('inf')
        for i in range(1, n + 1):
            # not_break --> move up n - i
            # break --> move down i - 1
            res = min(res, max(self.dfs(k, n - i, memo), self.dfs(k - 1, i - 1, memo)) + 1)

        memo[(k, n)] = res
        return memo[(k, n)]


class Solution:  # top down + binary search
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        return self.dfs(k, n, memo)

    def dfs(self, k, n, memo):
        if (k, n) in memo:
            return memo[(k, n)]

        # base case --> one egg, need to try n times to find
        if k == 1:
            return n

        if n <= 1:
            return n

        res = float('inf')
        left, right = 1, n
        while left <= right:
            mid = (right - left) // 2 + left
            # not_break --> move up n - i
            # break --> move down i - 1
            up = self.dfs(k, n - mid, memo)
            down = self.dfs(k - 1, mid - 1, memo)
            if down > up:
                right = mid - 1
            else:
                left = mid + 1
            res = min(res, max(up, down) + 1)

        memo[(k, n)] = res
        return memo[(k, n)]


class Solution2:
    def superEggDrop(self, k, n):
        # dp[i][j]表示用i次trial 和 j个鸡蛋,最多可以测试的楼层的高度
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # 可检测的楼层 = （break）上一次可检测的楼层 + 0 +（not_break）下次可检测的楼层 + 1
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
            # 如果可以检测到 n 层了，停止
            if dp[i][j] >= n:
                return i

