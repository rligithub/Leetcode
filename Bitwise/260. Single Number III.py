class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # step1：找出 异或 不同的地方
        diff = 0
        for num in nums:
            diff ^= num
        # step2: 从右到左，找出xor值为1的位置，分为两组
        div = 1
        while diff & div == 0:
            div = div << 1

            # step3: 找出两组中分别的xor
        res = [0, 0]
        for num in nums:
            if num & div == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res