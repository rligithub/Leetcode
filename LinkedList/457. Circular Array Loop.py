class Solution: # slow + fast pointers 
    def circularArrayLoop(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            slow = i
            fast = self.getNext(nums, i)

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[self.getNext(nums, fast)] > 0:
                if slow == fast:
                    if slow != self.getNext(nums, slow):  # 避免死循环，卡死在 nums[i] = 0 上 原地踏步
                        return True
                    else:
                        break
                slow = self.getNext(nums, slow)
                fast = self.getNext(nums, self.getNext(nums, fast))

        return False

    def getNext(self, nums, i):
        n = len(nums)
        return (i + nums[i]) % n

