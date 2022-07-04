class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        # 重复三个数的抵消，只有一个数出现一次，求该数
        # 数一下每个位置上的1的个数，看是否能够被3整除，不是的话 在该位置上标上1
        # 注意 negative的数字判断
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            if count % 3 != 0:
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res 