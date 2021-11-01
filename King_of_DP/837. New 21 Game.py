class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 从n个数值为[1, maxPts]中选牌，牌面总和大于等于k，停止抽排，求最后的牌面总和小于n的概率
        # k <= total_sum <= n
        # probability  of total_sum that is between k and n

        memo = {}
        return self.dfs(n, k, maxPts, 0, memo)

    def dfs(self, n, k, maxPts, cur_sum, memo):
        if cur_sum in memo:
            return memo[cur_sum]

        # 如果等于k，则不能抽排。 ===》 必须在k-1的时候停下来，看抽的最后一张牌的大小
        # n - k + 1 指的是 满足 k<= 最后一张牌 <= n 的个数有几个 ==》 最后这一张牌的prob
        if cur_sum == k - 1:
            return min(n - k + 1, maxPts) / maxPts

        # 不符合条件
        if cur_sum > n:
            return 0

            # 符合条件
        if cur_sum >= k:
            return 1

        # f(16) ==>     17 18 19 20 21 22 23 24 25  26
        # f(15) ==> 16  17 18 19 20 21 22 23 24 25
        # f(16) - f(15) = 26 - 16
        # f(x) - f(x-1) = (f(x+w) - f(x)) / w
        # f(x-1) = f(x) - (f(x+w) - f(x)) / w
        prob = self.dfs(n, k, maxPts, cur_sum + 1, memo) - (
                    self.dfs(n, k, maxPts, cur_sum + 1 + maxPts, memo) - self.dfs(n, k, maxPts, cur_sum + 1,
                                                                                  memo)) / maxPts

        memo[cur_sum] = prob
        return memo[cur_sum]


class Solution2:  # TLE
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 从n个数值为[1, maxPts]中选牌，牌面总和大于等于k，停止抽排，求最后的牌面总和小于n的概率
        # k <= total_sum <= n
        # possibility of total_sum that is between k and n

        memo = {}
        return self.dfs(n, k, maxPts, 0, memo)

    def dfs(self, n, k, maxPts, cur_sum, memo):
        if cur_sum in memo:
            return memo[cur_sum]

        if cur_sum >= k:
            if cur_sum <= n:
                return 1
            else:
                return 0

        prob = 0
        for i in range(1, maxPts + 1):
            prob += self.dfs(n, k, maxPts, cur_sum + i, memo) / maxPts

        memo[cur_sum] = prob
        return memo[cur_sum]














