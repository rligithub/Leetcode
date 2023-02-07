class Solution1:  # space O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        # count how many positive num
        containsOne = False
        positive = 0
        positiveNum = set()
        for num in nums:
            if num > 0:
                positive += 1
                positiveNum.add(num)
            if num == 1:
                containsOne = True

        if not containsOne:  # edge case
            return 1

        for i in range(1, positive + 1):
            if i not in positiveNum:
                return i
        return i + 1


class Solution:  # indexing sort + space O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:

        # replace all negative num and zero to n+1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # use indexing to check mark down existing num --> num in specific indexing will be marked as negative
        for i in range(n):
            index = abs(nums[i])
            if index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        # for loop each index to see which num are not marked down as negative --> return index
        for index in range(n):  # from small to large
            if nums[index] > 0:
                return index + 1

        return n + 1  # no missing, return n+1



