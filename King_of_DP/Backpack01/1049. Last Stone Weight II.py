class Solution:  # top down dp
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 给一堆石头，每次选两个石头 对消 差值变成新石头。求最小 对消后的剩下的石头 --> min diff
        # 类似题：加正负号
        # eg. 2 2 1 1 1 6
        memo = {}
        return self.dfs(stones, 0, 0, memo)

    def dfs(self, stones, pos, s, memo):
        if (pos, s) in memo:
            return memo[(pos, s)]

        # end of array, return the current sum (abs)
        if pos == len(stones):
            return abs(s)

        # add negative sign vs not_add negative sign
        not_add = self.dfs(stones, pos + 1, s + stones[pos], memo)
        add = self.dfs(stones, pos + 1, s - stones[pos], memo)

        memo[(pos, s)] = min(not_add, add)
        return memo[(pos, s)]


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 给一堆石头，每次选两个石头 对消 差值变成新石头。求最小 对消后的剩下的石头 --> min diff
        # 要么加到左边 要么加到右边 求最小差值
        memo = {}
        return self.dfs(stones, 0, 0, 0, memo)

    def dfs(self, stones, pos, s1, s2, memo):
        if (pos, s1, s2) in memo:
            return memo[(pos, s1, s2)]

        # end of array, return the current sum (abs)
        if pos == len(stones):
            return abs(s1 - s2)

        left = self.dfs(stones, pos + 1, s1 + stones[pos], s2, memo)
        right = self.dfs(stones, pos + 1, s1, s2 + stones[pos], memo)

        memo[(pos, s1, s2)] = min(left, right)
        return memo[(pos, s1, s2)]