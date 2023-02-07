class Solution1:
    def minPatches(self, nums, n: int) -> int:

        covered, i = 0, 0
        res = 0
        while covered < n:
            num = nums[i] if i < len(nums) else float('inf')
            if num > covered + 1:
                covered = covered * 2 + 1
                res += 1
            else:
                covered += num
                i += 1
        return res

class Solution:
    def minPatches(self, nums, n: int) -> int:

        miss = 1
        i = 0
        count = 0
        while miss <= n:  # until cursum covers n
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1

            else:
                miss *= 2
                count += 1
                print(miss)
        return count


nums = [1, 5, 10]
n = 30
a = Solution1()
print(a.minPatches(nums, n))