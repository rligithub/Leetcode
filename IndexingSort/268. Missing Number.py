class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR --> same num will be zero ---> use current nums ^ (1..n)
        mask = len(nums)  # 注意 number的取值范围为 0 ... n-1， n取代了missing的那一位，所以初始值设为 n
        for i, num in enumerate(nums):
            mask = mask ^ i ^ num

        return mask


class Solution: # indexing sort
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i, num in enumerate(nums):
            index = abs(num)
            if i == 0 and index == 0 or (index >= n):
                continue

            if index == 0:
                nums[index] = - nums[index]
                nums[i] = n

            elif nums[index] == 0:
                nums[0] = - nums[0]
                nums[index] = -n
            else:
                nums[index] = - abs(nums[index])

        for i in range(n):
            if nums[i] > 0:
                return i
        return n