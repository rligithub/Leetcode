class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        tail = collections.Counter()    # save length of subsequence ending at num
        for num in nums:
            if counter[num] and tail[num-1]: # 可以衔接
                counter[num]-=1
                tail[num-1]-=1
                tail[num]+=1
                # continue
            elif counter[num] and counter[num+1] and counter[num+2]: # 可以生成新序列
                tail[num+2] += 1
                counter[num] -= 1
                counter[num+1] -= 1
                counter[num+2] -= 1
                # continue
            elif counter[num]:
                return False
        return True