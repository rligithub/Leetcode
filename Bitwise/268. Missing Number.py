class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR --> same num will be zero ---> use current nums ^ (1..n)
        mask = len(nums)  # 注意 number的取值范围为 0 ... n-1， n取代了missing的那一位，所以初始值设为 n
        for i, num in enumerate(nums):
            mask = mask ^ i ^ num

        return mask