class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 骑士救公主 向下 or 向右 走 --> health + dungeon[i][j] > 0
        # health 需要大于 （0 - dungeon[i][j] + 1） 一点血来维持生命
        # 注意 中途不能挂掉 ==> res must alway greater than 0
        memo = {}
        return self.dfs(dungeon, 0, 0, memo)

    def dfs(self, dungeon, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over range
        if i == len(dungeon) or j == len(dungeon[0]):
            return float('inf')

        # base case --> health 永远大于 0
        # 如果只有一步，是补药 --> 需要1点血来活着（0点就挂掉了）--> health = 1
        # 如果只有一步，是毒药 --> 则需要 -毒药 的血来 消耗毒药，还需要1点血来活着 --> health = - dungeon[i][j] + 1
        if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
            return max(1, -dungeon[i][j] + 1)

        health = min(self.dfs(dungeon, i + 1, j, memo), self.dfs(dungeon, i, j + 1, memo)) - dungeon[i][j]
        # 使得 health 永远大于 0
        health = max(health, 1)

        memo[(i, j)] = health
        return memo[(i, j)]
