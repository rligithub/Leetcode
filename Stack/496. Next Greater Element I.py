class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 维持一个递减的stack --> 每次递增的时候算一遍, 把stack.pop()的数存起来 {stack[-1]: cur_num}

        hashmap = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            if num in hashmap:
                res.append(hashmap[num])
            else:
                res.append(-1)

        return res

