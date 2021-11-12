class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # TWO CASES:
        # CASE1 - put it in cur_row, update h and w
        # CASE2 - put it in nxt_row
        # row --> current row
        # h --> current row height
        # w --> current row remaining width
        # res --> accumlated prev heights
        n = len(books)
        memo = {}

        return self.dfs(books, shelfWidth, 0, 0, shelfWidth, memo)

    def dfs(self, books, shelfWidth, row, h, w, memo):
        if (row, h, w) in memo:
            return memo[(row, h, w)]

        if w < 0:
            return float('inf')

        if row == len(books):
            return h

        w1, h1 = books[row]
        pick_cur = self.dfs(books, shelfWidth, row + 1, max(h1, h), w - w1, memo)
        pick_nxt = self.dfs(books, shelfWidth, row + 1, h1, shelfWidth - w1, memo) + h

        memo[(row, h, w)] = min(pick_cur, pick_nxt)
        return memo[(row, h, w)]





