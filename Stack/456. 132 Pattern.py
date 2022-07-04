class Solution:  # stack
    def find132pattern(self, nums: List[int]) -> bool:
        # min, max, mid ---> 从尾部开始，即先维持一个单调递增的stack，mid --> max ，每次进来一个数字，如果比mid小，即找到min，return，否则就更新mid的值尽量使其最大，stack只要maintain一个max的值就可以
        stack = []
        mid = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid:
                return True

            while stack and stack[-1] < nums[i]:
                mid = stack.pop()

            stack.append(nums[i])
        return False
