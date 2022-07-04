class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 保留k位数 使其最小 --> 即 删掉 n - k位数，使其最小 same to #402 remove k digits
        k = len(nums) - k
        if k >= len(nums):
            return []

        stack = []

        for digit in nums:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k:  # if there is remaining k
            stack.pop()
            k -= 1


        return stack