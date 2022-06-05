class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a * x * x + b * x + c

        n = len(nums)
        if a < 0:
            index = 0
        else:
            index = n - 1

        l, r = 0, n - 1
        ans = [0] * n

        while l <= r:
            numl, numr = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if numl > numr:
                    ans[index] = numl
                    l += 1
                else:
                    ans[index] = numr
                    r -= 1
                index -= 1
            else:
                if numl > numr:
                    ans[index] = numr
                    r -= 1
                else:
                    ans[index] = numl
                    l += 1
                index += 1
        return ans