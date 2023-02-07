class Solution: # greedy
    def jump(self, nums: List[int]) -> int:
        # 每次更新cur 可跳到范围内能跳最远的地方，判断当前cur和i的位置，在for loop到cur之前的位置都是1步，到当前cur的位置 才count++，然后更新cur到能跳到的最远的位置 ---> 减少jump次数
        count = 0
        cur = 0
        maxjump = 0
        for i, num in enumerate(nums[:-1]):
            # we continuously find the how far we can reach in the current jump
            maxjump = max(maxjump, i + num)
            # if we have come to the end of the current jump,
            # we need to make another jump
            if i == cur:
                count += 1
                cur = maxjump
            print(i, num, maxjump, cur, count)
        return count