class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # guess target num --> check if there is k num less than target

        left, right = matrix[0][0], matrix[-1][-1]

        while left <= right:
            mid = left + (right - left) // 2
            if self.getNumOfSmaller(matrix, mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getNumOfSmaller(self, matrix, target):
        # count num of num in matrix that is smaller than target --> find right boundary --> see where mid == to
        m, n = len(matrix), len(matrix[0])
        count = 0
        for i in range(m):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[i][mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            count += left

        return count


