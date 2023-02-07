class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 给一个数组，求 最少要sort多少长度的subarry 使得整个array是sorted好的 ---> 先sort好整个array，然后比较，找出left index 和 right index
        sorted_nums = sorted(nums)

        left, right = -1, -1
        for i in range(len(nums)):
            if sorted_nums[i] == nums[i]:
                continue
            if left == -1:
                left = i
            else:
                right = i

        if left == -1 and right == -1:
            return 0
        return right - left + 1



