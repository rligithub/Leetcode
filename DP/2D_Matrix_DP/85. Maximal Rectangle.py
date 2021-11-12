class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 滚动数组 + maintain一个最大矩阵值
        # 滚动到下一层，遇到 0  等于0； 遇到1，加上1
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [0] * n

        res = 0
        # transition formula
        for i in range(m):
            for j in range(n):
                # next level ==> dp[j] =?
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] += 1
                # 求最大矩阵
            res = max(res, self.largestrectangle(dp))
        return res

    def largestrectangle(self, arr):

        # 维持一个stack，存的是index值
        # 如果 arr[i] >= arr[stack[-1]], 添加 arr[i]到stack
        # 如果 arr[i] < arr[stack[-1]], 计算area，pop stack的值，直到arr[i] >= stack[-1], 添加 arr[i]到stack
        # 计算area --> 高为stack最高的那个数，宽为stack存的末尾index到(i-1)的距离 ==》 h = stack.pop() ; w = i-1 - stack[-1]

        # 多添加一个值 0 在 arr的末尾，index值为 -1 ==> 保证stack不为空
        arr.append(0)
        stack = [-1]

        res = 0
        for i in range(len(arr)):
            while arr[i] < arr[stack[-1]]:
                h = arr[stack.pop()]
                w = i - 1 - stack[-1]
                res = max(res, h * w)
            stack.append(i)
        return res

