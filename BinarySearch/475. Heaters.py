class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # find first positions
        # for loop each houses --> find closest heaters --> find max

        heaters = sorted(heaters)
        res = 0

        for house in houses:
            index = self.findInsertPos(heaters, house)
            if index == len(heaters):
                res = max(res, house - heaters[-1])
            elif index == 0:
                res = max(res, heaters[0] - house)
            else:
                res = max(res, min(heaters[index] - house, house - heaters[index - 1]))

        return res

    def findInsertPos(self, nums, target):  # find first position that greater/equal to target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left




