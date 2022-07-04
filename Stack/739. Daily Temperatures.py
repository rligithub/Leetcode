class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        hashmap = {}
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                hashmap[stack.pop()] = i

            stack.append(i)

        res = []
        for i, temp in enumerate(temperatures):
            if i in hashmap:
                res.append(hashmap[i] - i)
            else:
                res.append(0)
        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pos = stack.pop()
                res[pos] = i - pos

            stack.append(i)

        return res 