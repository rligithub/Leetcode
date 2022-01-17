class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # hashmap --> { manager: empoyees }
        # 每下一层是 存 下一个通知的employee和通知到它所需的累积时间--> 找一个通知到每个人的最大时间

        employees = collections.defaultdict(list)

        for i in range(n):
            if i == headID:
                continue
            employees[manager[i]].append(i)

        queue = collections.deque()
        queue.append((headID, 0))
        res = 0

        while queue:
            cur, time = queue.popleft()
            res = max(res, time)
            for pp in employees[cur]:
                queue.append((pp, time + informTime[cur]))

        return res


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # hashmap --> { manager: empoyees }
        # 每下一层是 存 下一个通知的employee和通知到它所需的累积时间--> 找一个通知到每个人的最大时间
        employees = collections.defaultdict(list)

        for i in range(n):
            if i == headID:
                continue
            employees[manager[i]].append(i)

        self.res = 0
        self.dfs(headID, employees, informTime, 0, 0)
        return self.res

    def dfs(self, head, employees, informTime, time, count):
        if count == len(informTime):
            return

        time += informTime[head]
        count += 1

        self.res = max(self.res, time)

        for pp in employees[head]:
            self.dfs(pp, employees, informTime, time, count)

