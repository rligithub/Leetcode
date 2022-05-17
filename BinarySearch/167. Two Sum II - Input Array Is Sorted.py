class Solution: #binary search 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            left, right = i + 1, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    right = mid - 1
                else:
                    left = mid + 1
        return [-1, -1]
