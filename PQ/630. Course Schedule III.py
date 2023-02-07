class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        n = len(courses)
        projects = []
        for i in range(n):
            duration, lastDay = courses[i]
            projects.append((lastDay, duration))
        projects.sort()  # sort by lastDay

        curDay = 0
        count = 0
        heap = []

        for lastDay, duration in projects:
            curDay += duration
            heapq.heappush(heap, - duration)
            while curDay > lastDay:
                curDay += heapq.heappop(heap)  # 把不符合条件的pop掉

        return len(heap)