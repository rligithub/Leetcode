class Solution1:  # hashmap
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)

        k = len(nums) / 3

        res = []
        for num in freq.keys():
            if freq[num] > k:
                res.append(num)
        return res


class Solution:  # greedy
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 如果同时消去数组中互不相同的三个数，那么在剩下的数组中，超过1/3的那些数仍然是超过1/3的。所以我们只要不停找到三个互不相同的数并做消去，剩下的就是超过1/3的那些数（最多两个）
        if not nums:
            return []

        # 1st pass
        count1, count2, num1, num2 = 0, 0, None, None
        for num in nums:
            if num1 == num:
                count1 += 1
            elif num2 == num:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 += 1
            elif count2 == 0:
                num2 = num
                count2 += 1
            else:  # 消去数组中互不相同的三个数
                count1 -= 1
                count2 -= 1

        # 2nd pass
        res = []
        for num in [num1, num2]:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res