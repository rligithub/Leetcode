class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # heap ---> pop top k large sum

        maxSum = sum(x for x in nums if x > 0)
        heap = [(-maxSum, 0)]
        vals = sorted(abs(x) for x in nums)

        for _ in range(k):
            curSum, i = heappop(heap)
            if i < len(vals):
                heappush(heap, (curSum + vals[i], i + 1))  # continue minus cur val

                if i:
                    heappush(heap, (
                    curSum - vals[i - 1] + vals[i], i + 1))  # only minus cur val (need to add back prev substraction)
        return -curSum