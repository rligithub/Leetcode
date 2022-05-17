class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search target
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid // n][mid % n]
            if cur == target:
                return True
            elif cur > target:
                right = mid - 1  # 当前的mid已经判断过了比target小，则从mid-1 到 0
            else:
                left = mid + 1  # 当前的mid已经判断过了比target大，则从mid + 1 到结束
        return False