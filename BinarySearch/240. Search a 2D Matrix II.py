class Solution1:  # for loop + binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find target in 2D matrix --> for loop row + binary search col
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

