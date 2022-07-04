class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = collections.deque()
        res = float('-inf')

        for i in range(len(points)):
            while queue and points[i][0] - points[queue[0]][0] > k:
                queue.popleft()

            # ensure points y - x in queue[0] is max --> so max summ
            if queue:
                res = max(res, points[i][1] + points[queue[0]][1] + points[i][0] - points[queue[0]][0])

                # maintain max (y - x) in queue[0]
            while queue and points[i][1] - points[i][0] > points[queue[-1]][1] - points[queue[-1]][0]:
                queue.pop()

            queue.append(i)

        return res