class Solution1:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left = 0
        right = 1

        count = 0

        while left < n and right < n:
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                count += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

        return count


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)

        res = 0
        for num in count.keys():
            if k == 0:
                if count[num - k] > 1:
                    res += 1
            else:
                if num - k in count:
                    res += 1
        return res