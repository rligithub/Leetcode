
class Solution  :# heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # start our heap with the first element from every single list
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)

        minn, maxx = float('-inf'), float('inf')
        curMax = max(row[0] for row in nums)

        while heap:
            curMin, i, j = heapq.heappop(heap)
            if curMax - curMin < maxx - minn:   # if there is smaller range --> update
                minn, maxx = curMin, curMax

            if j + 1 == len(nums[i]):   # return
                return [minn, maxx]

            # add new num + update curMax
            next_num = nums[i][ j +1]
            heapq.heappush(heap, (next_num, i, j + 1))
            curMax = max(curMax, next_num)

