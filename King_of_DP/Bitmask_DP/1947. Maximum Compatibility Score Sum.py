class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        # similar to # 1879 Minimum XOR sum of two array --> 2D now
        memo = {}
        return self.dfs(students, mentors, 0, 0, memo)

    def dfs(self, students, mentors, state, s, memo):
        if (state, s) in memo:
            return memo[(state, s)]

        if s == len(students):
            return 0

        res = float('-inf')
        for m in range(len(mentors)):
            if state & (1 << m) == 0:
                res = max(res,
                          self.dfs(students, mentors, state | (1 << m), s + 1, memo) + self.score(students, mentors, s,
                                                                                                  m))

        memo[(state, s)] = res
        return memo[(state, s)]

    def score(self, students, mentors, s, m):
        count = 0
        for i in range(len(students[s])):
            count += (students[s][i] == mentors[m][i])

        return count