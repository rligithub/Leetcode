class Solution1:  # top down dp1
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # 下棋，从右下角S出发 到左上角E结束，可以往上走，往左走，左斜走。
        # return 最大sum 和 几种方式可以得到最大sum
        # 类似题 673. Number of Longest Increasing Subsequence

        # dfs --> 同时分别求 最大sum 和 几种方式
        memo = {}
        maxval, count = self.dfs(board, len(board) - 1, len(board[0]) - 1, memo)
        mod = 10 ** 9 + 7
        if maxval != float('-inf'):
            return [maxval % mod, count % mod]
        else:
            return [0, 0]

    def dfs(self, board, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over the range
        if i < 0 or j < 0 or board[i][j] == 'X':
            return float('-inf'), 0
        # base case
        if i == 0 and j == 0 and board[i][j] == 'E':
            return 0, 1

        # recursive
        v1, c1 = self.dfs(board, i, j - 1, memo)
        v2, c2 = self.dfs(board, i - 1, j, memo)
        v3, c3 = self.dfs(board, i - 1, j - 1, memo)
        maxval = max(v1, v2, v3)

        count = 0
        for x, y in ((v1, c1), (v2, c2), (v3, c3)):
            if x == maxval:
                count += y

        if board[i][j] != 'S':
            val = int(board[i][j])
        else:
            val = 0

        memo[(i, j)] = maxval + val, count
        return memo[(i, j)]


class Solution:  # top down dp2
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        memo = {}
        maxval, count = self.dfs(board, len(board) - 1, len(board[0]) - 1, memo)
        mod = 10 ** 9 + 7
        if maxval != float('-inf'):
            return [maxval % mod, count % mod]
        else:
            return [0, 0]

    def dfs(self, board, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i < 0 or j < 0 or board[i][j] == 'X':
            return float('-inf'), 0

        if i == 0 and j == 0 and board[i][j] == 'E':
            return 0, 1

        if board[i][j] != 'S':
            cur_val = int(board[i][j])
        else:
            cur_val = 0

        maxval = float('-inf')
        count = 0
        for dx, dy in ((0, -1), (-1, 0), (-1, -1)):
            # 为什么不在dfs后面直接加board[i][j] --->因为dfs返回是两个值，count是不能加board[i][j]DE
            val, cnt = self.dfs(board, i + dx, j + dy, memo)

            if val + cur_val > maxval:
                maxval = val + cur_val
                count = cnt
            elif val + cur_val == maxval:
                count += cnt

        memo[(i, j)] = maxval, count
        return memo[(i, j)]
