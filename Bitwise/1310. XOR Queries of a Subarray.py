class Solution1:  # TLE
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        res = []

        for i, j in queries:
            num = 0
            for k in range(i, j + 1):
                num ^= arr[k]
            res.append(num)
        return res


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # prefix XOR
        xors = [0]
        for num in arr:
            xors.append(xors[-1] ^ num)

        res = []
        for i, j in queries:
            res.append(xors[j + 1] ^ xors[i])
        return res