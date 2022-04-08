class Solution1:
    def containVirus(self, grid: List[List[int]]) -> int:
        # step1: for loop --> similar to num of island --> bfs to get (infected_positions, nxt_infected_positions, walls_count)
        # step2: visited += infected_position, record [(infected_positions, nxt_infected_positions, walls_count)] for each group --> find max size of nxt_infected positions, record the index to get wall_counts --> build wall for infected_positions, infect virus for nxt_infected_positions, res += wall counts
        # step3: early break if no nxt_infected_positions

        m, n = len(grid), len(grid[0])

        res = 0
        while True:
            visited = set()
            max_area_num = 0
            record_idx = 0
            cur_infected_areas = []
            next_infected_areas = []
            wall_lens = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        infected, nxt_infected, wall = self.getCurAndNextInfectedArea(grid, i, j, m, n)  # 得到该感染区域能感染的面积

                        for x, y in infected:  # 将当前感染的区域设置为已访问
                            visited.add((x, y))

                        cur_infected_areas.append(infected)
                        next_infected_areas.append(nxt_infected)
                        wall_lens.append(wall)

                        area_num = len(nxt_infected)  # 找出下一个最大被感染的区域
                        if area_num > max_area_num:
                            max_area_num = area_num
                            record_idx = len(next_infected_areas) - 1  # 记录最大被感染区域的 index
            if max_area_num > 0:
                res += wall_lens[record_idx]  # 防火墙的长度不等于（！！！）将要感染的面积
                for x, y in cur_infected_areas[record_idx]:  # 将record_idx对应感染区域的数值标为2，作为不会再扩散的标记
                    grid[x][y] = 2

                for idx in range(len(next_infected_areas)):  # 其他感染区域进行扩散
                    if idx != record_idx:
                        for x, y in next_infected_areas[idx]:
                            grid[x][y] = 1
            else:
                break

        return res

    def getCurAndNextInfectedArea(self, grid, x, y, m, n):
        # 获取当前感染的区域以及下一次会感染的相邻区域，以及需要的防火墙长度
        queue = collections.deque()
        queue.append((x, y))
        infected = set()
        infected.add((x, y))

        nxt_infected = set()

        wall_count = 0

        while queue:
            i, j = queue.popleft()

            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:  # 将要被感染
                        nxt_infected.add((x, y))
                        wall_count += 1
                    elif grid[x][y] == 1:  # 相邻感染的区域
                        if (x, y) not in infected:
                            queue.append((x, y))
                            infected.add((x, y))

        return infected, nxt_infected, wall_count

