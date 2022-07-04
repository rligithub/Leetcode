class Solution:  # XOR --> bit
    def singleNumber(self, nums: List[int]) -> int:
        # XOR --> same num will be zero

        mask = 0
        for num in nums:
            mask = mask ^ num
        return mask


class Solution1:  # hashset
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        for res in seen:
            return res