class Solution:  # BFS
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 给对应的ID 和下属ID，求指定ID 及其所有下属的importance value和

        # build graph
        graph = collections.defaultdict(list)
        value = collections.defaultdict(int)

        for employee in employees:
            for sub in employee.subordinates:
                graph[employee.id].append(sub)
            value[employee.id] = employee.importance

        # do bfs
        queue = collections.deque()
        queue.append(id)

        res = 0
        while queue:
            cur_id = queue.popleft()
            res += value[cur_id]

            for nei in graph[cur_id]:
                queue.append(nei)
        return res
