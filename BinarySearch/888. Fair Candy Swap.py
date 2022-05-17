class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # find 1/2 of total sum ---> check if any of diff would be in bobSizes --> binary search to find target

        aliceSizes.sort()
        bobSizes.sort()

        summA = sum(aliceSizes)
        summB = sum(bobSizes)
        summ = (summA + summB) // 2

        for num in aliceSizes:
            target = summ - (summA - num)
            if self.binarySearch(bobSizes, target) != -1:
                return [num, target]

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1