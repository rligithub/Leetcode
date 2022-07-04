"""

2,1,3,4,4
2 3 6
1 2 3 4 4
1 3 6



"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        nums = sorted(arr)
        sum1, sum2 = 0, 0

        res = 0
        for num1, num2 in zip(arr, nums):
            sum1 += num1
            sum2 += num2
            if sum1 == sum2:
                res += 1
        return res

#         stack = []
#         for num in arr:
#             largest = num

#             while stack and stack[-1] > num:
#                 largest = max(largest, stack.pop())

#             stack.append(largest)

#         return len(stack)

