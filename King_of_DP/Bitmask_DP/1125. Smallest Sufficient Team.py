class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # dp --> 每种required skills是否有需求--> 11111 有需要求
        # 求出每个人是否能满足哪些required skills
        # for loop 每个人，看下一个人能否有 remaining required skill，有的话 在team中 加入此人的index
        # 比较team大小，使得team中的人数最少

        m = len(req_skills)
        n = len(people)

        # convert each person's skills to bitmask
        req_table = {}
        for i, skill in enumerate(req_skills):
            req_table[skill] = i

        peopleMask = [0] * n
        for i, person in enumerate(people):
            for skill in person:
                if skill in req_table:
                    peopleMask[i] |= 1 << req_table[skill]

        memo = {}
        return self.dfs(peopleMask, (1 << m) - 1, 0, memo)

    def dfs(self, peopleMask, fullMask, state, memo):
        if state in memo:
            return memo[state]

        if state == fullMask:
            return []

        res = [0] * (len(peopleMask) + 1)  # intialization max # of people in the team
        for i in range(len(peopleMask)):
            nxtState = state | peopleMask[i]
            if nxtState == state:
                continue
            if len(res) > len(self.dfs(peopleMask, fullMask, nxtState, memo)):
                res = self.dfs(peopleMask, fullMask, nxtState, memo) + [i]
        memo[state] = res
        return memo[state]



