from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        string = []
        for num in nums:
            string.append(str(num))

        string.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

        if string[0] == "0":
            return "0"
        return "".join(string)