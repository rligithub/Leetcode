
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


class Solution: # heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # maintain k size heap --> get curMin
        # append next num (at same row) to heap --> get/update curMax
        # record min(curMax - curMin) --> record maxx and minn
        # after j is the end of any row, return maxx and minn

        heap = []
        curMax = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            curMax = max(curMax, nums[i][0])

        minn, maxx = float('-inf'), float('inf')
        while heap:
            curMin, i, j = heapq.heappop(heap)
            if curMax - curMin < maxx - minn:
                maxx, minn = curMax, curMin
            if j == len(nums[i]) - 1:
                return [minn, maxx]
            heapq.heappush(heap, (nums[i][j+1], i, j + 1))
            curMax = max(curMax, nums[i][j+1])
