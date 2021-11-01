class Solution:  # top down dp
    def stoneGameIII(self, stoneValue) -> str:
        # 一排石头，每个人可以从左边拿1-3个石头每次，拿完为止。总积分多的赢，求谁赢
        # memo --> values difference between first player and second player

        memo = {}
        score = self.dfs(stoneValue, 0, memo)
        print(score)
        if score == 0:
            return 'Tie'
        elif score < 0:
            return 'Bob'
        else:
            return 'Alice'

    def dfs(self, stoneValue, pos, memo):
        if pos in memo:
            return memo[pos]

        # corss line
        if pos > len(stoneValue) - 1:
            return 0

        res = float('-inf')
        score = 0
        for i in range(1, 4):
            # FIRST PLAYER SCORE
            if pos + i -1 > len(stoneValue) - 1:
                break
            score += stoneValue[pos + i - 1]
            # RES = FIRST PLAYER SCORE - SECOND PLAYER SCORE
            res = max(res, score - self.dfs(stoneValue, pos + i, memo))

        memo[pos] = res
        return memo[pos]



a = Solution()

stoneValue = [1,2,3,7]
print(a.stoneGameIII(stoneValue))


