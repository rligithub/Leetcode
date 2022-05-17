class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        if n1 > n2:
            arr1, arr2 = arr2, arr1
        if n1 > n3:
            arr1, arr3 = arr3, arr1

        res = []
        for num in arr1:
            if self.findTarget(arr2, num) and self.findTarget(arr3, num):
                res.append(num)
        return res

    def findTarget(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False