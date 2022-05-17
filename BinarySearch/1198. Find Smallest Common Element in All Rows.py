class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # similar to 1213 intersection of three sorted arrays
        m, n = len(mat), len(mat[0])

        for j in range(n):
            target = mat[0][j]
            found = True
            for i in range(1, m):
                pos = self.findTarget(mat[i], target)
                if pos == -1:
                    found = False
                    break
            if found:
                return target
        return -1

    def findTarget(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1



