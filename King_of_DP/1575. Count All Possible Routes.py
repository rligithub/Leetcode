class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 给一个起始位置和终点位置，和油量。求有几种不同的路径到终点位置

        # variables: cur_city, fuel
        # pick or not pick

        memo = {}
        return self.dfs(locations, finish, start, fuel, memo)

    def dfs(self, locations, finish, city, fuel, memo):
        if (city, fuel) in memo:
            return memo[(city, fuel)]

        if fuel < 0:
            return 0

        if city == finish:
            res = 1
        else:
            res = 0

        mod = 10 ** 9 + 7

        for nextCity in range(len(locations)):
            if nextCity == city:
                continue
            res += self.dfs(locations, finish, nextCity, fuel - abs(locations[nextCity] - locations[city]), memo)

        memo[(city, fuel)] = res % mod
        return memo[(city, fuel)]


