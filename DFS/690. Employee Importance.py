"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = collections.defaultdict(list)
        values = collections.defaultdict(int)

        for employee in employees:
            i, val, sub = employee.id, employee.importance, employee.subordinates
            for ee in sub:
                graph[i].append(ee)
            values[i] = val

        self.res = 0
        self.dfs(graph, values, id)
        return self.res

    def dfs(self, graph, values, node):
        self.res += values[node]
        for nei in graph[node]:
            self.dfs(graph, values, nei)

