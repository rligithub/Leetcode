'''
    -- j ---->
    A'  B'  C'
A   1   3   5
B   4   1   1
C   1   5   3

step1: Connect all points in the left column to right column, find find min cost to connect
step2: Markdown which points in right column was connected, use bitmask
step3: When all points in left column is connected (pos == m), check if there is any points in right column that is unconnected(check bitmask)
step4: Find min cost to connect to right point

'''


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])

        # get min cost of connecting to right column
        min_arr = [min([cost[i][j] for i in range(m)]) for j in range(n)]

        print(min_arr)
        memo = {}
        return self.dfs(cost, min_arr, 0, 0, memo)

    def dfs(self, cost, min_arr, pos, mask, memo):
        if (pos, mask) in memo:
            return memo[(pos, mask)]

        m, n = len(cost), len(cost[0])

        if pos == m:
            res = 0
            for j in range(n):
                # 有个没连上
                if mask & (1 << j) == 0:
                    res += min_arr[j]
            memo[(pos, mask)] = res
            return memo[(pos, mask)]

        res = float('inf')
        for j in range(n):
            res = min(res, self.dfs(cost, min_arr, pos + 1, mask | (1 << j), memo) + cost[pos][j])

        memo[(pos, mask)] = res
        return memo[(pos, mask)]