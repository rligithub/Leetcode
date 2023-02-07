class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        projects = []
        for i in range(n):
            startTime = tasks[i][0]
            processTime = tasks[i][1]
            projects.append((startTime, processTime, i))
        projects.sort()  # sort by startTime

        curTime = 0
        i = 0
        heap = []
        res = []
        while i < n or heap:
            if not heap and curTime < projects[i][0]:
                curTime = projects[i][0]

            while i < n and curTime >= projects[i][
                0]:  # available projects when curTime is passed startTime, push all available to heap
                startTime, processTime, idx = projects[i]
                heapq.heappush(heap, (processTime, idx))
                i += 1
            processTime, idx = heapq.heappop(heap)  # pop smaller processTime
            curTime += processTime
            res.append(idx)

        return res
