class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        minn = []
        maxx = []
        cur_min = float('inf')
        i = -1
        for num in nums:
            if num < cur_min:
                cur_min = num
            else:
                i = self.binarySearch(num, maxx)
                if i > 0 and num > minn[i - 1]:
                    return True
                if i < len(maxx):
                    maxx[i] = num
                    minn[i] = cur_min
                else:
                    maxx.append(num)
                    minn.append(cur_min)
        return False

    def binarySearch(self, target, nums):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid
        return right


