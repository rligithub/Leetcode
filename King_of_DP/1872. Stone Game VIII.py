class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 拿石头，每次需要拿两堆以上最左侧的石头，拿完后 把合并的石头堆 作为一堆放在最左侧
        # prefsum --> 1st player find the max , 2nd player find the second max

        n = len(stones)
        prefsum = [0] * n
        prefsum[0] = stones[0]
        for i in range(1, n):
            prefsum[i] = prefsum[i - 1] + stones[i]

        memo = {}
        return self.dfs(prefsum, 1, memo)

    def dfs(self, prefsum, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(prefsum) - 1:
            return prefsum[pos]

            # 1st player picks or not pick current prefsum --> choose bigger prefsum
        pick = prefsum[pos] - self.dfs(prefsum, pos + 1, memo)
        not_pick = self.dfs(prefsum, pos + 1, memo)

        memo[pos] = max(pick, not_pick)
        return memo[pos]