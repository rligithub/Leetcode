class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # 安装一个广告牌，这有两个支架，每个支架高度相等。求最大高度
        # for each rod --> CASE1: add it to left
        #                   CASE2: add it to right
        #                   CASE3: not add
        # dfs -- > return sum of (left rods + right rods)
        # if diff == 0 and pos == len(rod) ===> return 0

        memo = {}
        return self.dfs(rods, 0, 0, memo) // 2

    def dfs(self, rods, pos, diff, memo):
        if (pos, diff) in memo:
            return memo[(pos, diff)]

        if pos == len(rods):
            if diff == 0:
                return 0
            else:
                return float('-inf')

        pick_left = self.dfs(rods, pos + 1, diff + rods[pos], memo) + rods[pos]
        pick_right = self.dfs(rods, pos + 1, diff - rods[pos], memo) + rods[pos]
        not_pick = self.dfs(rods, pos + 1, diff, memo)

        memo[(pos, diff)] = max(pick_left, pick_right, not_pick)
        return memo[(pos, diff)]



