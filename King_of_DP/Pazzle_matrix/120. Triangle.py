class Solution1:  # slower
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle, pos, row, memo):
        if (pos, row) in memo:
            return memo[(pos, row)]

        # over the range
        if row == len(triangle):
            return 0

        # base case
        if row == len(triangle) - 1:
            return triangle[0][0]

        res = min(self.dfs(triangle, pos, row + 1, memo) + triangle[row + 1][pos],
                  self.dfs(triangle, pos + 1, row + 1, memo) + triangle[row + 1][pos + 1])

        memo[(pos, row)] = res
        return memo[(pos, row)]


class Solution:  # faster
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle, pos, row, memo):
        if (pos, row) in memo:
            return memo[(pos, row)]

        # base case
        if row == len(triangle) - 1:
            return triangle[row][pos]

        res = min(self.dfs(triangle, pos, row + 1, memo), self.dfs(triangle, pos + 1, row + 1, memo)) + triangle[row][
            pos]

        memo[(pos, row)] = res
        return memo[(pos, row)]