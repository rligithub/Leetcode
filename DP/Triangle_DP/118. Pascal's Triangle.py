class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # 建一个杨辉三角的矩阵
        dp = [[1] * x for x in range(1, numRows + 1)]

        # 杨辉三角的规律： dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # 0 <= i < n ; 1 <= j < i

        # 第1行和第2行 --> 值为0

        # 第3...n-1行 --> 第0和i+1列 值为0 ； 第1...i列的值为上面两个的和
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp

