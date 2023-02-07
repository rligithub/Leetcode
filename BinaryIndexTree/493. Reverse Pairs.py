class BinaryIndexTree:
    def __init__(self, n):
        self.summ = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        while i < len(self.summ):
            self.summ[i] += val
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.summ[i]
            i -= self.lowbit(i)
        return res


class Solution:  # similar to # 315
    def reversePairs(self, nums: List[int]) -> int:
        newNums = nums + [num * 2 for num in nums]

        sortedNums = sorted(list(set(newNums)))
        index = {}
        for i, num in enumerate(sortedNums):
            index[num] = i + 1

        tree = BinaryIndexTree(len(sortedNums))
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            res += tree.query(index[nums[i]] - 1)
            tree.update(index[nums[i] * 2], 1)  # Tree 里存的是从右往左 nums[j]*2，这样for loop到左边 nums[i]位置就可以直接和nums[j]*2位置上比较
        return res



import sortedcontainers
import bisect

class Solution: # sorted list  + binary search  --> O(n*(log(n)+log(n)) --> O(nlog(n))
    def reversePairs(self, nums: List[int]) -> int:
        # nums[i] >= 2 * nums[j]   ===> find 2*cur_num in prev nums
        # i < j     ==> use a sorted_list to store all prev nums
        prev_arr = sortedcontainers.SortedList()

        count = 0
        for j in range(len(nums)):
            target = 2*nums[j]
            pos = prev_arr.bisect_right(target)
            count += len(prev_arr) - pos

            prev_arr.add(nums[j])

        return count
