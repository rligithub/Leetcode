class Solution:  # kmp
    def strStr(self, haystack: str, needle: str) -> int:

        prefix = self.KMP(needle)

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            print(i, j)
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                if j != 0:
                    j = prefix[j - 1]
                else:
                    i += 1

        if j == len(needle):
            return i - len(needle)

        return -1

    def KMP(self, nums):
        n = len(nums)
        prefix = [0] * n

        cnt = 0
        i = 1
        while i < n:
            if nums[i] == nums[cnt]:
                cnt += 1
                prefix[i] = cnt
                i += 1
            else:
                if cnt != 0:
                    cnt = prefix[cnt - 1]
                else:
                    prefix[i] = 0
                    i += 1
        print(prefix)
        return prefix