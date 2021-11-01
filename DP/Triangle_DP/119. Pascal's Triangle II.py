class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 杨辉三角，给行的index值，打印最后一行的数
        dp = [[1] * x for x in range(1, rowIndex + 2)]

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        return dp[-1]