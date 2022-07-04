class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        visited = {}
        while n > 0:
            nums = tuple(cells)
            if nums in visited:
                n %= visited[nums] - n
            visited[nums] = n

            if n >= 1:
                n -= 1
                cells = self.nextday(cells)

        return cells

    def nextday(self, cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]