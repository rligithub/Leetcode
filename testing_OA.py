
#
# def DaysBetween(year1, month1, day1, year2, month2, day2):
#     period1 = year1 * 365 + day1
#
#     # Add days for months in given date
#     for i in range(0, month1 - 1):
#         period1 += DaysInMonth[i]
#
#
#     period2 = year2 * 365 + day2
#     for i in range(0, month2 - 1):
#         period2 += DaysInMonth[i]
#
#     return (period2 - period1)
#
#
#
# def DaysInMonth(month, year):
#     leap = 0
#     if year % 400 == 0:
#         leap = 1
#     elif year % 100 == 0:
#         leap = 0
#     elif year % 4 == 0:
#         leap = 1
#     if month == 2:
#         return 28 + leap
#     list = set(1, 3, 5, 7, 8, 10, 12)
#     if month in list:
#         return 31
#     return 30
#
#
#
#
#
# test = [2010,5,1,2011,5,1]
# year1, month1, day1, year2, month2, day2 = test
# print(DaysBetween(year1, month1, day1, year2, month2, day2))



import collections

path = ""
def validTree(string):
    if not string or string[0] == " " or string[-1] == " ":
        return "E1"        # invalid input

    # check one line!!!!!!

    edges = string.split(" ")

    indegree = collections.defaultdict(int)
    outdegree = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    seen = set()
    size = set()
    for pair in edges:
        if len(pair) != 5 or pair[0] != "(" or pair[2] != "," or pair[4] != ")" or pair[1] == pair[3]:
            raise E1        # invalid input

        if pair[1].islower() or not pair[3].islower():
            raise E1        # invalid input
        if pair in seen:
            raise E2        # duplicated pairs
        seen.add(pair)
        p, c = pair[1], pair[3]
        indegree[c] += 1
        outdegree[p] += 1
        if indegree[c] > 1:
            raise E4        # more than one root
        if outdegree[p] > 2:
            raise E3        # more than 2 children

        graph[p].append(c)
        size.add(p)
        size.add(c)

    queue = collections.deque()
    for i in indegree.keys():
        if indegree[i] == 0:
            queue.append(i)

    count = 0
    while queue:
        cur = queue.popleft()
        count += 1
        for nei in graph[cur]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    if count != len(size):
        return getPath()
    else:
        raise E5





    visited = set()
    hasCycle = dfs(graph, 0, -1, visited)
    if hasCycle:
        raise E5

    elif len(visited) == len(size):
        raise E4

    else:
        return path


def dfs(self, neighbors, i, visited):
    if i in visited:  # visited --> check has cycle
        return False

    visited.add(i)

    for nei in neighbors[i]:
        if not self.dfs(neighbors, nei, visited):
            return False
    return True



graph = [(a,b),(b,c),(a,e),(b,d)]
print(getString(graph))

















