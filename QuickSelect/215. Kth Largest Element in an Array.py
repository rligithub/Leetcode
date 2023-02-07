class Solution1:  # nlogn
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # binary search num --> check if there is k num greater or equal to it

        left, right = min(nums), max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getGreaterCount(nums, mid, k) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def getGreaterCount(self, nums, target, k):
        count = 0
        for num in nums:
            if num >= target:
                count += 1
            if count >= k:
                return count
        return count


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use quick selection to sort the array, return nums[k-1]
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, left, right, k):
        pivot = self.partition(nums, left, right)
        if pivot == k - 1:
            return nums[pivot]
        elif pivot < k - 1:
            return self.quickSelect(nums, pivot + 1, right, k)
        else:
            return self.quickSelect(nums, left, pivot - 1, k)

    def partition(self, nums, left, right):
        if len(nums) == 0:
            return 0
            # randomly select a num from array, swap it to last index
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]

        # use two pointers for same direction, make sure number bigger than pivot is always in left side of slow pointer --> sort by large to smaller
        slow = left
        for fast in range(left, right):
            if nums[fast] > nums[right]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        nums[slow], nums[right] = nums[right], nums[slow]

        return slow