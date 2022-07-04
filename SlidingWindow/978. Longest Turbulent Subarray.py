class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = cur = 0

        for i in range(len(arr)):
            if i >= 2 and (arr[i - 2] > arr[i - 1] < arr[i] or arr[i - 2] < arr[i - 1] > arr[i]):
                cur += 1
            elif i >= 1 and arr[i - 1] != arr[i]:
                cur = 2
            else:
                cur = 1
            res = max(res, cur)
        return res

